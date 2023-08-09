#23tree.py
#By: Sam Schmitz and Ryan Neubauer
#a class for 2-3 trees

class Tree23:

    def __init__(self, keys=[]):
        self.tree = _node23()
        for k in keys:
            self.insert(k)

    def insert(self, item):
        result = self.tree._insert(item)
        if result is not None:
            #print("new root node")
            key, left, right = result
            self.tree = _node23(key, [left, right])

    def __contains__(self, key):
        return (key in self.tree)

    def __iter__(self):
        return iter(self.tree)

    def pretty_print(self): #let the node do this
        self.tree._pretty_print()

class _node23:

    def __init__(self, key=None, trees=[]):
        if key is not None:
            self.keys = [key]
        else:
            self.keys = []
        self.trees = list(trees)

    def _key_scan(self, key):   #find which sub tree you are working on
        i = 0
        while (i < len(self.keys)) and (self.keys[i] < key):
            i = i + 1
        return i

    def _pretty_print(self, tabs=0):
        for i in range(tabs):   #print the numebr of tabs without moving to the next line
            print("\t", end="")
        print(self.keys)
        if self.trees != []:
            for i in self.trees:    #prettyprint sub trees indented by one
                i._pretty_print((tabs+1))

    def _insert(self, item): #conect an element to a node
        if self.trees == []:  #check if the node has any children/is end of a branch
            if self.keys == []: #if the node is empty
                self.keys.append(item)
            else:
                if self.keys[0] > item: #if it does not add the item to the node
                    self.keys.insert(0, item)
                elif self.keys[-1] < item:
                    self.keys.append(item)
                else:
                    self.keys.insert(1, item)
                if len(self.keys) > 2:  #if the node contains 3 nodes split and return
                    #print("node returning", self.keys)
                    return (self.keys[1], _node23(self.keys[0]), _node23(self.keys[2]))
        else:     #if it does place the node in one of the children
            subTree = self._key_scan(item)
            #print("subtree =", subTree, "item =", item)
            result = self.trees[subTree]._insert(item)
            if result is not None:  #if a new node is returned add that data to this node
                key, left, right = result
                self.trees.pop(subTree) #remove the subTree so that the new parts can be added
                self.trees.insert(subTree, right)   #add left and right where the old sub tree was
                self.trees.insert(subTree, left)
                #print("subTrees added", self.trees)
                if self.keys[0] > key:  #insert the key into the node
                    self.keys.insert(0, key)
                elif self.keys[-1] < key:
                    self.keys.append(key)
                else:
                    self.keys.insert(1, key)
                if len(self.keys) > 2:  #if there are more than 2 keys in the node split and promote
                    #print("node returning", self.keys)
                    return self.keys[1], _node23(self.keys[0], [self.trees[0], self.trees[1]]), _node23(self.keys[2], [self.trees[2], self.trees[3]])

    def __contains__(self, key):
        if key in self.keys:    #check the keys in this node
            return True
        for i in self.trees:    #check the keys in the branches
            if key in i:
                return True
        return False

    def __iter__(self):
        if self.trees == []:    #base case if there are no branches
            for i in self.keys: #return the keys
                yield i
        else:
            for i in range(len(self.keys)): #loop through for each key
                it = iter(self.trees[i])    #yield the keys in the sub tree
                while True:
                    try:
                        yield (next(it))
                    except:
                        break
                yield self.keys[i]  #yeild the key and loop
            it = iter(self.trees[-1])   #yield the last sub tree
            while True:
                try:
                    yield (next(it))
                except:
                    break


if __name__ == "__main__":
    t = Tree23()
    t.insert(3)
    print(list(t))
    t.insert(1)
    t.insert(5)
    t.insert(2)
    t.insert(4)
    t.insert(6)
    t.insert(0)
    t.insert(1)
    y = Tree23([3, 1, 4, 5, 9, 2, 6])
    print("5 in y:", (5 in y))
    print("10 in y:", (10 in y))
    print(list(y))
    y.pretty_print()
    y.insert(0)
    y.insert(10)
    print("10 in y:", (10 in y))
    y.pretty_print()
    t2 = Tree23(range(1,16))
    t2.pretty_print()
    t3 = Tree23(["a", "b", "c"])
    t3.pretty_print()
