import random
import time

def bubbleSort(arr):
    n = len(arr)

    for i in range(n - 1):

        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def bubbleSortRe(arr):
    n = len(arr)

    for i in range(n - 1):

        for j in range(0, n - i - 1):

            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

arr = []

#LOSOWANIE LICZBA DO TABLICY
start = time.time()
for i in range(300000):
    arr.append(random.randint(0,100))

print(arr)
end = time.time()
print(f"Runtime of the program is {end - start}")
print(" ")

#SORTOWANIE BĄBELKOWE
start = time.time()
bubbleSort(arr)
print(arr)
end = time.time()
print(f"Runtime of the program is {end - start}")
print(" ")

#SORTOWANIE BĄBELKOWE ODWROTNE
start = time.time()
bubbleSortRe(arr)
print(arr)
end = time.time()
print(f"Runtime of the program is {end - start}")
