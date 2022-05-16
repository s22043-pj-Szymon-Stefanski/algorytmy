import random
import time

#quicksort
def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)

def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[j], A[i] = A[i], A[j]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1

#ODWROTNY quicksort
def quicksortRe(A, p, r):
    if p < r:
        q = partitionRe(A, p, r)
        quicksortRe(A, p, q - 1)
        quicksortRe(A, q + 1, r)

def partitionRe(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] >= x:
            i += 1
            A[j], A[i] = A[i], A[j]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1

arr = []
arr1 = []
arr2 = []
arr3 = []

#LOSOWANIE LICZBA DO TABLICY
start = time.time()
for i in range(90000):
    arr.append(random.randint(0,100))
for i in range(90000):
    arr1.append(random.randint(0,100))
for i in range(90000):
    arr2.append(random.randint(0,100))
for i in range(90000):
    arr3.append(random.randint(0,100))
#Potrzeba wykorzystania czterech różnych list z powodu błędu:
#RecursionError: maximum recursion depth exceeded in comparison
#WYNIK CZASU - SUMA WSZYSTKICH LOSOWAŃ
end = time.time()
print(f"Runtime of the program is {end - start}")
print(" ")

#quicksort
#WYNIK CZASU - SUMA WSZYSTKICH SORTOWAŃ
start = time.time()
quicksort(arr, 0, len(arr) - 1)
quicksort(arr1, 0, len(arr) - 1)
quicksort(arr2, 0, len(arr) - 1)
quicksort(arr3, 0, len(arr) - 1)
end = time.time()
print(f"Runtime of the program is {end - start}")

#Odwrotny quicksort
#WYNIK CZASU - SUMA WSZYSTKICH SORTOWAŃ
start = time.time()
quicksortRe(arr, 0, len(arr) - 1)
quicksortRe(arr1, 0, len(arr) - 1)
quicksortRe(arr2, 0, len(arr) - 1)
quicksortRe(arr3, 0, len(arr) - 1)
end = time.time()
print(f"Runtime of the program is {end - start}")
