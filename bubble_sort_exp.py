#bubble_sort_exp.py
#By: Sam Schmitz
#A version of the bubble sort algorithm that stops when a loop is completed without a exchange
#The main function then compares the original to the expirement

import time, random

def bubble_sort_exp(A):
    b = 1   #create a variable that will tell if a change has taken place
    for i in range(len(A) - 1):
        for j in range(len(A) - 1 - i):
            if A[j+1] < A[j]:
                A[j], A[j+1] = A[j+1], A[j]
                b = 0   #show that a change has taken place
        if b >= 1:  #check for a change
            return   #if no change break
        #print(A)   #prints the list after the loop
        b = 1   #reset to no change

def bubble_sort(A): #sorts using the bubble sort algoritm
    for i in range(len(A) - 1): #reach all elements in the list
        for j in range(len(A) - 1 - i): #reach all elements that havn't been set yet
            if A[j+1] < A[j]:   #if the element after is greater swap
                A[j], A[j+1] = A[j+1], A[j]

def crtLst(lstSz):
    l = []
    for i in range(lstSz):
        l.append(random.randrange(1, 1000))
    return l    #creates a random list with the size of lstSz

def main():
    print("This program compares the speeds of the Bubble Sort Algorithm and an Expiremental one")
    print("Enter the test list size: ", end="")
    lstSz = int(input())
    print("Enter the number of trials: ", end="")
    trials = int(input())
    print("")

    print("Original Bubble Sort: ")
    total = 0   #do the number of trials for the regular bubble sort
    for i in range(trials):
        lst = crtLst(lstSz)
        start = time.time()
        bubble_sort(lst)
        end = time.time()
        tTime = end - start
        total += tTime
        print("trial %s: %d" %(i+1, tTime))
    print("total: %s \n" %total)
    print("average:", (total/trials), "\n")

    print("Experimental Bubble Sort: ")
    totalExp = 0    #do the numebr of trials for the expiremental bubble sort
    for i in range(trials):
        lst = crtLst(lstSz)
        start = time.time()
        bubble_sort_exp(lst)
        end = time.time()
        tTime = end - start
        totalExp += tTime
        print("trial %s: %d" %(i+1, tTime))
    print("total: %s \n" %totalExp)
    print("average:", (totalExp/trials), "\n")

    if (total > totalExp):
        print("The Expiremental Bubble Sort was Faster")
    else:
        print("The Original Bubble Sort was Faster")


main()
