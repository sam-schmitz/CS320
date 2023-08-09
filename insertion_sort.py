#insertion_sort.py
#By: Sam Schmitz
#an Implementation of the insertion sort algorithm

def insertion_sort(A):
    for i in range(len(A)):
        v = A[i]
        j = i - 1
        while j >= 0 and A[j] > v:
            A[j+1] = A[j]
            j = j - 1
        A[j + 1] = v

def main():
    lst = [2, 6, 3, 8, 1]
    insertion_sort(lst)
    print(lst)

main()
