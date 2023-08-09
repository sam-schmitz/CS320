#pq.py
#By: Sam Schmitz
# An implementation of the Priority Queue data structure

class PriorityQueue:
    def __init__(self, items=[]):
        self.heap = list(items)
        self._build_heap()

    def _largest_child(self, i):    #returns index of node i's largest child or None when node i is a leaf
        lChild, rChild = (2*i + 1), (2*i + 2)
        try:    #try to find the greatest of the 2 indexes
            if self.heap[lChild] >= self.heap[rChild]:
                return lChild
            return rChild
        except: #if the right child doesn't exist
            try:    #look to see if the left most is a real index
                self.heap[lChild]
                return lChild
            except: #accept that the node is a leaf
                return None

    def _bubble_up(self, i):    #restore heap by bubbling up from node i
        while i > 0:
            pi = (i-1) // 2
            if self.heap[i] <= self.heap[pi]:
                break
            self.heap[i], self.heap[pi] = self.heap[pi], self.heap[i]
            i = pi

    def _bubble_down(self, i):  #restore heap by bubbling down from node i
        k = self._largest_child(i)
        if k and self.heap[k] > self.heap[i]:
            self.heap[k], self.heap[i] = self.heap[i], self.heap[k]
            self._bubble_down(k)

    def _build_heap(self):  #builds an initial heap bottom-up
        i = len(self.heap) - 1
        #print(self.heap)
        while i != -1:
            self._bubble_down(i)
            #print(self.heap, i)
            i = i - 1

    def add(self, item):    #add item to the Queue
        self.heap.append(item)
        self._bubble_up(len(self.heap) - 1)

    def get_max(self):  #returns and removes highest priority item
        item = self.heap[0]
        self.heap[0] = self.heap[-1]    #item from the end (remove)
        self.heap.pop(-1)
        self._bubble_down(0)
        return item

def heapsort(lst):  #uses a heap to sort the items in a list
    h = PriorityQueue(lst)
    #print(h.heap)
    sortLst = []
    for i in range(len(lst)):
        sortLst.insert(0, h.get_max())
    return sortLst

if __name__ == "__main__":
    lst = [3, 2, 5, 7, 1, 4, 6]
    nLst = heapsort(lst)
    print(nLst)
