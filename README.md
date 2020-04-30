# Fundamentals

A repo to keep track of my understanding of some CS fundamentals. I will be adding notes and implementations where applicable.

## Quick reference tables

### Sorting algorithms

Algorithm|Best case|Average case|Worst case|Stable|In place|Implementation|Remarks
-|-|-|-|-|-|-|-
Selection sort|-|-|-|-|-|-|-
Insertion sort|-|-|-|-|-|-|-
Bubble sort|-|-|-|-|-|-|-
Shell sort|-|-|-|-|-|-|-
[Merge sort](https://github.com/ChrisKneller/fundamentals#merge-sort)|O(½ *n* log *n*)|O(*n* log *n*)|O(*n* log *n*)|Yes|No|[Python](https://github.com/ChrisKneller/fundamentals/blob/master/sorting/mergesort.py)|-
Quick sort|-|-|-|-|-|-|-
Heap sort|-|-|-|-|-|-|-

## Data structures

### Linked Lists

### Trees, Tries & Graphs

### Heaps

### Vectors / ArrayLists

### Hash Tables

## Algorithms

### Bread-First Search

### Depth-First Search

### Binary Search

### Merge Sort

#### Summary
First divide the list into the smallest unit (1 element), then compare each element with the adjacent list to sort and merge the two adjacent lists. Finally all the elements are sorted and merged.

#### Notes
- A divide and conquer algorithm
- Stable (in most implementations)
- Does not sort in place (in most implementations - see [block merge sort](https://en.wikipedia.org/wiki/Block_merge_sort) for in place)

#### Key details
Best case|Average case|Worst case
-|-|-
O(½ *n* log *n*)|O(*n* log *n*)|O(*n* log *n*)

#### Diagram
![](https://upload.wikimedia.org/wikipedia/commons/e/e6/Merge_sort_algorithm_diagram.svg)

#### My implementation(s)
[Python, using deques](https://github.com/ChrisKneller/fundamentals/blob/master/sorting/mergesort.py)

### Quick Sort

## Concepts

### Bit Manipulation

### Memory (Stack vs. Heap)

### Recursion

### Dynamic Programming

### Big O Time & Space
