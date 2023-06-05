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

#LOSOWANIE LICZBA DO TABLICY
start = time.time()
for i in range(500000):
    arr.append(random.randint(0,100))

end = time.time()
print(f"Runtime of the program is {end - start}")
print(" ")

#quicksort
start = time.time()
quicksort(arr, 0, len(arr) - 1)
end = time.time()
print(f"Runtime of the program is {end - start}")

#Odwrotny quicksort
start = time.time()
quicksortRe(arr, 0, len(arr) - 1)
end = time.time()
print(f"Runtime of the program is {end - start}")
