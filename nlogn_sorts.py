#nlogn_sorts.py
#By: Sam Schmitz
#Implementations of merge sort and quick sort
#run some tests that they are nlogn(use a table)

from other_sorts import *
import random, time

def mergeSort(lst):
    #print(lst, len(lst))
    if int(len(lst)) > 1:
        #print(lst, len(lst))
        x = int((len(lst) / 2))
        lst2 = lst[0:x]
        lst3 = lst[x:None]
        #print(lst, lst2, lst3)
        lst2 = mergeSort(lst2)
        lst3 = mergeSort(lst3)
        lst = merge(lst2, lst3)
    return lst

def merge(b, c):    #redo with only b and c, and define p and q
    a = []
    i, j, k = 0, 0, 0
    p = len(b)
    q = len(c)
    while i < p and j < q:
        if b[i] <= c[j]:
            a.append(b[i])
            i = i + 1
        else:
            a.append(c[j])
            j += 1
        k = k + 1
    if i == p:
        for i in c[j:q]:
            a.append(i)
    else:
        for i in b[i:p]:
            a.append(i)
    list = [i, p, j, q]
    #print(b, c, a, list)
    return a

def quickSort(lst): #an Implementation of the quick sort algorithm
    _quickSort(lst, 0, (len(lst) - 1))

def _quickSort(lst, l, r):   #A helper function for quickSort
    print(f"quicksort: {lst}")
    if l < r:
        s = hoarePartition(lst, l, r)
        _quickSort(lst, l, (s-1))
        _quickSort(lst, (s+1), r)

def hoarePartition(lst, l, r):  #an Implementation of the Hoare Partition algorithm
    p = lst[l]
    i = l - 1
    j = r
    while True:
        while True:
            i = i + 1
            if lst[i] >= p:
                break
        while True:
            j = j - 1
            if lst[j] <= p:
                break
        lst[i], lst[j] = lst[j], lst[i]
        if i >= j:
            break
    lst[i], lst[j] = lst[j], lst[i]
    lst[l], lst[j] = lst[j], lst[l]
    return j

def medianPart(lst, l, r):
    #find the pivot
    pass


def findMed(lst, l, r):
    mid = (l + r - 1) // 2
    i = lst[l]
    j = lst[mid]
    k = lst[r - 1]
    if (i <= j <= k) or (k <= j <= i):
        return j, mid
    if (i <= k <= j) or (j <= k <= i):
        return k, (r-1)
    return i, l

def crtLst(lstSz):
    l = []
    for i in range(lstSz):
        l.append(random.randrange(1, 1000))
    return l    #creates a random list with the size of lstSz

def main():
    print("This program compares different sorting algorithms")
    print("Enter the list size: ", end="")
    lstSz = int(input())
    print("Enter the number of trials: ", end="")
    trials = int(input())
    print("")
    _trial(quickSort, trials, lstSz)
    _trial(mergeSort, trials, lstSz)
    _trial(count_sort, trials, lstSz)
    _trial(bubble_sort, trials, lstSz)
    _trial(selection_sort, trials, lstSz)

def _trial(function, trials, lstSz):    #conduct a trial for a given function
    total = 0
    for i in range(trials): #gather the times for the trials
        lst = crtLst(lstSz)
        start = time.time()
        function(lst)
        end = time.time()
        tTime = end - start
        total += tTime
        print("trial %s: %d" %(i+1, tTime))
    print("total: %s" %total)
    print("average: %s \n" %(total/trials))

def main2():
    lst = [3, 4, 7, 5, 1, 6, 2, 8, 9, 10]
    print(lst)
    quickSort(lst)
    print(lst)
    lst2 = [3, 4, 7, 5, 1, 6, 2, 8, 9, 10]
    print(lst2)
    lst2 = mergeSort(lst2[0:])
    print(lst2)

main2()
