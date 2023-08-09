#bubble_sort.py
#By: Sam Schmitz
#implements the bubble sort algoritm

def bubble_sort(A): #sorts using the bubble sort algoritm
    for i in range(len(A) - 1): #reach all elements in the list
        for j in range(len(A) - 1 - i): #reach all elements that havn't been set yet
            if A[j+1] < A[j]:   #if the element after is greater swap
                A[j], A[j+1] = A[j+1], A[j]

def main():
    lst = [3, 2, 1, 4, 6, 5]
    bubble_sort(lst)
    print(lst)

main()
