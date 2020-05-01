# Fundamentals

A repo to keep track of my understanding of some CS fundamentals. I will be adding notes and implementations where applicable.

## Quick reference tables

### Sorting algorithms

Algorithm|Best case|Average case|Worst case|Stable|In place|Code|Remarks
-|-|-|-|-|-|-|-
Selection sort|-|-|-|-|-|-|-
Insertion sort|-|-|-|-|-|-|-
Bubble sort|-|-|-|-|-|-|-
Shell sort|-|-|-|-|-|-|-
[Merge sort](https://github.com/ChrisKneller/fundamentals/blob/master/README.md#merge-sort)|O(½ *n* log *n*)|O(*n* log *n*)|O(*n* log *n*)|Yes*|No*|[Python](https://github.com/ChrisKneller/fundamentals/blob/master/sorting/mergesort.py)|-
[Quick sort](https://github.com/ChrisKneller/fundamentals/blob/master/README.md#quick-sort)|O(*n* log *n*)|O(2*n* ln *n*)|O(½ *n*<sup>2</sup>)|No*|Yes*|[Python](https://github.com/ChrisKneller/fundamentals/blob/master/sorting/quicksort.py)|Worst case is rare
Heap sort|-|-|-|-|-|-|-

\* Further information can be seen in the sections dedicated to each sort.

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
- A [divide-and-conquer](https://en.wikipedia.org/wiki/Divide-and-conquer_algorithm) algorithm
- Stable (in most implementations)
- Does not sort in-place (in most implementations - see [block merge sort](https://en.wikipedia.org/wiki/Block_merge_sort) for in place)

#### Key details
Best case|Average case|Worst case
:-:|:-:|:-:
O(½ *n* log *n*)|O(*n* log *n*)|O(*n* log *n*)

#### Diagram
![](https://upload.wikimedia.org/wikipedia/commons/e/e6/Merge_sort_algorithm_diagram.svg)

#### My implementation(s)
[Python, using deques](https://github.com/ChrisKneller/fundamentals/blob/master/sorting/mergesort.py)

[Python, using pointers (reduced space complexity)](https://github.com/ChrisKneller/fundamentals/blob/master/sorting/mergesort.py#L53)

#### References
[David Taylor: Algorithms with Attitude](https://www.youtube.com/watch?v=k3oezbZgfDs) (fantastic explainer video on optimisations etc.)

### Quick Sort

#### Summary
Select a 'pivot' element from the array and partition the other elements into two sub-arrays, according to whether they are less than or greater than the pivot. The sub-arrays are then sorted recursively. This can be done in-place, requiring small additional amounts of memory to perform the sorting.

#### Notes
- A [divide-and-conquer](https://en.wikipedia.org/wiki/Divide-and-conquer_algorithm) algorithm
- Not stable for efficient implementations
- Does sort in-place

#### Key details
Best case|Average case|Worst case
:-:|:-:|:-:
O(*n* log *n*)|O(2*n* ln *n*)|O(½*n*<sup>2</sup>)

#### Diagram
![](https://upload.wikimedia.org/wikipedia/commons/6/6a/Sorting_quicksort_anim.gif)

#### My implementation(s)
[Python](https://github.com/ChrisKneller/fundamentals/blob/master/sorting/quicksort.py)

## Concepts

### Bit Manipulation

### Memory (Stack vs. Heap)

### Recursion

### Dynamic Programming

### Big O Time & Space
