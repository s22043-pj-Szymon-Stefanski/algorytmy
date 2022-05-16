import random
import time

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2

        L = arr[:mid]
        R = arr[mid:]

        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

#Odwrotny merge sort
def mergeSortRe(arr):
    if len(arr) > 1:
        mid = len(arr) // 2

        L = arr[:mid]
        R = arr[mid:]

        mergeSortRe(L)
        mergeSortRe(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] > R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


arr = []
#LOSOWANIE LICZBA DO TABLICY
start = time.time()
for i in range(300000):
    arr.append(random.randint(0,100))
print(arr)
end = time.time()
print(f"\nRuntime of the program is {end - start}")

#merge sort
start = time.time()
mergeSort(arr)
print("Sorted array is: ", end="\n")
printList(arr)
end = time.time()
print(f"\nRuntime of the program is {end - start}")

#Odwrotny merge sort
start = time.time()
mergeSortRe(arr)
print("Sorted array is: ", end="\n")
print(arr)
end = time.time()
print(f"\nRuntime of the program is {end - start}")
