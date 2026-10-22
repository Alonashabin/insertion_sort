# -----------------------------------------
# Program: Insertion Sort
# Author: Alona Shabin
# Description:
# This program sorts an array using the
# Insertion Sort algorithm.
# -----------------------------------------

def insertion_sort(arr):
    # Traverse through elements starting from index 1
    for i in range(1, len(arr)):
        key = arr[i]          # Current element
        j = i - 1

        # Move elements greater than key
        # one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # Insert key at correct position
        arr[j + 1] = key


# Taking input
n = int(input("Enter number of elements: "))

arr = []

print("Enter the elements:")

for i in range(n):
    arr.append(int(input()))

# Sorting
insertion_sort(arr)

print("Sorted Array:")

for i in arr:
    print(i, end=" ")
