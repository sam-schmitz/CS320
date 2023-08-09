#other_sorts.py
#By: Sam Schmitz
#a collection of other sorts that I turned in with the last portfolio

def selection_sort(A):
    min = 0
    for i in range(len(A)-1):
        min = i
        j = i + 1
        #print(i)
        while j < len(A):
            if A[j] < A[min]:
                min = j
            j += 1
        A[min], A[i] = A[i], A[min]

def bubble_sort(A): #sorts using the bubble sort algoritm
    for i in range(len(A) - 1): #reach all elements in the list
        for j in range(len(A) - 1 - i): #reach all elements that havn't been set yet
            if A[j+1] < A[j]:   #if the element after is greater swap
                A[j], A[j+1] = A[j+1], A[j]

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
