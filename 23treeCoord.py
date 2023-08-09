#23treeCoord.py
#By Sam Schmitz
#An implementation of the 23Tree class that sorts points based on how close they are to a given point

import math

class Tree23Coord:

    def __init__(self, bPoint, points=[]):
        self.tree = _node23Coord(bPoint)
        self.bPoint = bPoint    #the base point to compare the other points too
        for k in points:
            print(k)
            self.insert(k)

    def insert(self, point):
        result = self.tree._insert(point)
        if result is not None:
            #print("new root node")
            key, left, right = result
            self.tree = _node23Coord(self.bPoint, key, [left, right])

    def __contains__(self, point):
        return (point in self.tree)

    def __iter__(self):
        return iter(self.tree)

    def pretty_print(self): #let the node do this
        self.tree._pretty_print()

class _node23Coord:

    def __init__(self, bPoint, point=None, trees=[]):
        self.bPoint = bPoint
        if point is not None:
            self.points = [point]
        else:
            self.points = []
        self.trees = list(trees)

    def _key_scan(self, key):   #find which sub tree you are working on
        i = 0
        while (i < len(self.points)) and (math.dist(self.points[i], self.bPoint) < math.dist(key, self.bPoint)):
            i = i + 1
        return i

    def _pretty_print(self, tabs=0):
        for i in range(tabs):   #print the numebr of tabs without moving to the next line
            print("\t", end="")
        print(self.points)
        if self.trees != []:
            for i in self.trees:    #prettyprint sub trees indented by one
                i._pretty_print((tabs+1))

    def _insert(self, p): #conect an element to a node
        if self.trees == []:  #check if the node has any children/is end of a branch
            if self.points == []: #if the node is empty
                self.points.append(p)
            else:
                if math.dist(self.points[0], self.bPoint) > math.dist(p, self.bPoint): #if it does not add the item to the node
                    self.points.insert(0, p)
                elif math.dist(self.points[-1], self.bPoint) < math.dist(p, self.bPoint):
                    self.points.append(p)
                else:
                    self.points.insert(1, p)
                if len(self.points) > 2:  #if the node contains 3 nodes split and return
                    #print("node returning", self.points, self.points[1])
                    return (self.points[1], _node23Coord(self.bPoint, self.points[0]), _node23Coord(self.bPoint, self.points[2]))
        else:     #if it does place the node in one of the children
            subTree = self._key_scan(p)
            #print("subtree =", subTree, "item =", item)
            result = self.trees[subTree]._insert(p)
            if result is not None:  #if a new node is returned add that data to this node
                key, left, right = result
                self.trees.pop(subTree) #remove the subTree so that the new parts can be added
                self.trees.insert(subTree, right)   #add left and right where the old sub tree was
                self.trees.insert(subTree, left)
                #print("subTrees added", self.trees)
                if math.dist(self.points[0], self.bPoint) > math.dist(key, self.bPoint):  #insert the key into the node
                    self.points.insert(0, key)
                elif math.dist(self.points[-1], self.bPoint) < math.dist(key, self.bPoint):
                    self.points.append(key)
                else:
                    self.points.insert(1, key)
                if len(self.points) > 2:  #if there are more than 2 keys in the node split and promote
                    #print("node returning", self.keys)
                    return self.points[1], _node23Coord(self.bPoint, self.points[0], [self.trees[0], self.trees[1]]), _node23Coord(self.bPoint, self.points[2], [self.trees[2], self.trees[3]])

    def __contains__(self, key):
        if key in self.points:    #check the keys in this node
            return True
        for i in self.trees:    #check the keys in the branches
            if key in i:
                return True
        return False

    def __iter__(self):
        if self.trees == []:    #base case if there are no branches
            for i in self.points: #return the keys
                yield i
        else:
            for i in range(len(self.points)): #loop through for each key
                it = iter(self.trees[i])    #yield the keys in the sub tree
                while True:
                    try:
                        yield (next(it))
                    except:
                        break
                yield self.points[i]  #yeild the key and loop
            it = iter(self.trees[-1])   #yield the last sub tree
            while True:
                try:
                    yield (next(it))
                except:
                    break


if __name__ == "__main__":
    point = 0, 0
    t = Tree23Coord(point)
    for i in range(10):
        p = i, i
        t.insert(p)
    t.pretty_print()
