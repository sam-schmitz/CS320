#selection_sort.py
#By: Sam Schmitz
#implements the selection sort algoritm

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

def main():
    lst = [3, 2, 1, 4, 6, 5]
    selection_sort(lst)
    print(lst)

main()
