# insertion_sort
Objective
Implement the Insertion Sort algorithm and analyze its time and space complexities.

Programming Language
Python

Algorithm
Start from the second element.
Store the current element as the key.
Compare the key with previous elements.
Shift larger elements one position to the right.
Insert the key at the correct position.
Repeat until the array is sorted.
How to Run
Install Python 3.

Open terminal.

Execute:

python insertion_sort.py
Enter the number of elements.

Enter the array elements.

View the sorted output.

Sample Input
6
64
25
12
22
11
90
Sample Output
11 12 22 25 64 90
Time Complexity
Case	Complexity
Best	O(n), Θ(n), Ω(n)
Average	O(n²), Θ(n²), Ω(n²)
Worst	O(n²), Θ(n²), Ω(n²)
Space Complexity
O(1)
Advantages
Simple to implement.
Efficient for small datasets.
Stable sorting algorithm.
In-place sorting.
Disadvantages
Inefficient for large datasets.
Time complexity becomes O(n²) for average and worst cases.
Course Outcome
CO1 – Analyze any given algorithm and express its time and space complexities using asymptotic notations.
