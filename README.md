# algos
This repo provides examples of algorithms

You can find code for different algos in python

-[Linear Search](#linear-search)
-[Binary Search](#binary-search)
-[Lucknumber](#lucky-number)
-[HeapSort](#heap-sort)
-[MergeSort](#merge-sort)

# Linear Search

Linear search is an algorithm where we can find element in an unsorted list.

iteration - n+1
comparision - n
 total = n+1+n = 2n+1 = O(n)

It takes time complexity of O(n)

Space complexity of n

you can run the following code by running: python3 linear.py

# Binary Search


Here the binary search is implemented in Python

The time complexity of binary search is O(logn)

where g(n) = n/2+n/2^2+n/2^3+...

n/2^k = 1

k=logn

O(logn)

# Lucky Number

A number is lucky if all digits of the number are different. How to check if a given number is lucky or not.
Examples: 
 

<pre>Input: n = 983
Output: true
All digits are different</pre>

# Heap Sort
Heap sort is sorting technique using balanced tree
the time complexity is O(logn)
# Merge Sort

Merge sort is sorting technique using recursive algo
the time complexity is O(nlogn)
## Pros of MergerSort::

    - MErge sort is suitable for large size of list
    - Merge Sort is suitable for linked list
    - Merge Sort Supports External Sorting ( We can merge external lists in chunks)
    - Merge sort is stable algorithm
## Cons of Merge Sort:
    - Extra space (not inplace sort)
    - No SMall Problem (Slower for small data)
    - Extra stack space for recursive operation
# QUick Sort

It is divide conquer algorithm
THe worst case is if list is already sorted O(n^2) if pivot is first element
Average complexity is O(nlogn)

Removing worst case of quick sort:
1. Always select middle element as pivot O(nlogn)
2. Select Random element as pivot O(n^2)

Space complexity::
It uses stack for recusrsive
Worst Case is O(n^2)
Best case O(logn) to O(n)


# Algorithms we can write under divide and conquer
     - Merge Sort
     - binary sort
     - Quick Sort


# Types of algorithms
    - Back tracking - Nqueen
    - Divide and Conquer - Merge,QUick Sort
    - Dynamic Programming - Fibonacci
    - Greedy Algorithm
    - Simple Recursive Algorithm - Tower of Hanoi or DFS
    - Branch and bound alogrithms
    - Brute force algorithnms
    - Randomized algorithms
