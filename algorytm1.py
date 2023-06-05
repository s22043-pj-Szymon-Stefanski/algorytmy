import random
import time

#KOPIEC
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[largest] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        heapify(arr, n, largest)


def heapSort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

#KOPIEC ODWROTNY
def heapifyRe(arr, n, i):
    smallest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[l] < arr[smallest]:
        smallest = l

    if r < n and arr[r] < arr[smallest]:
        smallest = r

    if smallest != i:
        (arr[i],
         arr[smallest]) = (arr[smallest],
                           arr[i])

        heapifyRe(arr, n, smallest)


def heapSortRe(arr, n):
    for i in range(int(n / 2) - 1, -1, -1):
        heapifyRe(arr, n, i)

    for i in range(n - 1, -1, -1):
        arr[0], arr[i] = arr[i], arr[0]

        heapifyRe(arr, i, 0)

def printArray(arr, n):
    for i in range(n):
        print(arr[i], end=" ")
    print()

arr = []

#LOSOWANIE LICZBA DO TABLICY
start = time.time()
for i in range(300000):
    arr.append(random.randint(0,100))

print(arr)
end = time.time()
print(f"Runtime of the program is {end - start}")
print(" ")

#KOPIEC
start = time.time()
heapSort(arr)
n = len(arr)
print("Kopiec:")
for i in range(n):
    print("%d" % arr[i], end=" ")
end = time.time()
print(f"\nRuntime of the program is {end - start}")
print(" ")

#KOPIEC ODWROTNY
start = time.time()
n = len(arr)
heapSortRe(arr, n)

print("Kopiec odwrotny: ")
printArray(arr, n)
end = time.time()
print(f"Runtime of the program is {end - start}")
