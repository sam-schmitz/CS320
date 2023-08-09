# compare_count_sort.py
# By: Sam Schmitz

import time, random

def count_sort(A):
    count = []
    n = len(A)
    for i in A:  #create a list containing a 0 for each value in A
        count.append(0)
    #print(count)
    s = count.copy()
    #print(s)
    for i in range(len(A)-1):   #for each num in the list except 1
        j = i + 1
        while (j < len(A)): #for each num in the list past than the A[i]
            #print(i, j)
            if A[i] < A[j]:
                count[j] += 1
            else:
                count[i] += 1
            j += 1
        #print(j)
    for i in range(n):
        #print(s, count[i], A[i])
        s[count[i]] = A[i]
    return s    #sorts a list by comparison counting

def crtLst(lstSz):
    l = []
    for i in range(lstSz):
        l.append(random.randrange(1, 1000))
    return l    #creates a random list with the size of lstSz

def main():
    print("Welcome to the Comparison Count Sorter\n")   #intro and data gathering
    print("Enter the list size: ", end="")
    lstSz = int(input())
    print("Enter the number of trials: ", end="")
    trials = int(input())
    print("")

    total = 0
    for i in range(trials): #gather the times for the trials
        lst = crtLst(lstSz)
        start = time.time()
        count_sort(lst)
        end = time.time()
        tTime = end - start
        total += tTime
        print("trial %s: %d" %(i+1, tTime))
    print("total: %s \n" %total)

    print("average:", (total/trials))   #print the average time

main()
