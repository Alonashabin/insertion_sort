# Insertion Sort in Python

**Author:**Alona Shabin

## 1. Objective

The objective of this program is to implement the Insertion Sort algorithm using Python. It sorts a list of integers in ascending order by placing each element in its correct position in the already-sorted portion of the list.

## 2. Description

Insertion Sort is a simple sorting algorithm that works similarly to arranging playing cards in your hand. It takes one element at a time and compares it with the previous elements. If the previous elements are greater than the current element, they are shifted one position to the right. The current element is then inserted into its correct position.

This process continues until all the elements are sorted.

## 3. Algorithm

1. Start.
2. Read the number of elements, `n`.
3. Read `n` integer elements and store them in an array.
4. Start from the second element of the array (index 1).
5. Store the current element in a variable called `key`.
6. Compare the key with the elements before it.
7. Shift all elements greater than the key one position to the right.
8. Insert the key into its correct position.
9. Repeat steps 5–8 until all elements have been processed.
10. Display the sorted array in ascending order.
11. Stop.

## 4. Advantages

- **Easy to understand:** The algorithm is simple and beginner-friendly.
- **Easy to implement:** It requires only a few lines of code.
- **In-place sorting:** It sorts the array without requiring another array.
- **Stable sorting:** Equal elements maintain their original relative order.
- **Efficient for small datasets:** It performs well when the number of elements is small.
- **Adaptive:** It works efficiently when the array is already or nearly sorted.

## 5. Disadvantages

- **Slow for large datasets:** It requires more time when sorting a large number of elements.
- **High time complexity in the worst case:** The worst-case time complexity is O(n²).
- **Many shifts:** Elements may need to be shifted several times to insert a key into its correct position.
- **Not suitable for large unsorted arrays:** More efficient algorithms, such as Merge Sort and Quick Sort, are generally preferred for large datasets.

## 6. Time and Space Complexity

| Case | Time Complexity |
|---|---|
| Best Case | O(n) |
| Average Case | O(n²) |
| Worst Case | O(n²) |

**Space Complexity:** O(1), because the algorithm sorts the array in place using a constant amount of additional memory.

## 7. Sample Input

```text
Enter number of elements: 5
Enter the elements:
8
3
5
1
4
```

## 8. Sample Output

```text
Sorted Array:
1 3 4 5 8
```

## 9. Applications

- Sorting small lists of elements.
- Sorting data that is already nearly sorted.
- Maintaining sorted lists when new elements are added.
- Serving as a component of more advanced sorting algorithms.

## 10. Conclusion

Insertion Sort is a simple and easy-to-understand sorting algorithm that arranges elements in ascending order. It is suitable for small or nearly sorted datasets because it is efficient in such cases and requires very little additional memory. However, its quadratic time complexity makes it less suitable for large datasets.

## 11.Course Outcome
CO1 – Analyze any given algorithm and express its time and space complexities using asymptotic notations.
