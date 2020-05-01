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

#### Comparison of my implementations
![Sorting comparison scatter plot](/sorting/plots/sorting_comparison.png)

## Data structures

### Linked Lists

### Trees, Tries & Graphs

#### Binary trees

- Trees in which each node has two or fewer children
- An extension of a linked list, where each node can be linked to two children rather than one (a linked list could be considered a "unary tree")
- The **root** is the single node at the top
- **Branches** connect nodes
- Nodes at the bottom (pointing to no other nodes) are called **leaves**
- Number of nodes = number of branches + 1
- The **depth of a node** is the number of branches from the node to the root (i.e. above)
- The **height of a node** is the number of branches from the node to its deepest descendant leaf
- The **tree height** is the number of branches from the root to the deepest leaf
- Largest number of nodes a binary tree can have if it has height *n* is **2<sup>*n*+1</sup> - 1** 
    - i.e. a tree of height 5 can have at most 2<sup>5+1</sup> - 1 = 2<sup>6</sup> - 1 = 64 - 1 = 63 nodes

```python
class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value # information that is being stored in the tree
        self.left = left   # the left child (subtree)
        self.right = right # the right child (subtree)

    def __str__(self):
        return str(self.value)
```

![Example of a binary tree](https://upload.wikimedia.org/wikipedia/commons/f/f7/Binary_tree.svg)

Root|No. branches|Leaves|Depth of node 7|Height of node 7|Tree height
:-:|:-:|:-:|:-:|:-:|:-:
2|8|2, 5, 11, 4|1|2|3

- A **full binary tree** is a binary tree in which each node has *exactly* zero or two children
    - A full binary tree will *always* have an odd number of nodes: 2 or 0 children for each node, plus the root

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Full_binary.svg/2560px-Full_binary.svg.png" alt="Full binary tree" width="200"/>

- A **complete binary tree** is a binary tree in which every level, except possibly the last, is completely filled and all nodes are as far left as possible

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Complete_binary2.svg/2880px-Complete_binary2.svg.png" alt="Complete binary tree (not full)" width="200"/>

- A tree can be *full but not complete* and a tree can be *complete but not full*

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
[Python, pivot at mid point](https://github.com/ChrisKneller/fundamentals/blob/master/sorting/quicksort.py)

[Python, pivot at random point](https://github.com/ChrisKneller/fundamentals/blob/master/sorting/quicksort.py#L17)

## Concepts

### Bit Manipulation

### Memory (Stack vs. Heap)

### Recursion

### Dynamic Programming

### Big O Time & Space
