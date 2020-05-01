from collections import deque
import numpy as np

def mergesort(iterable, final_length=False):
    '''
    Return a new list containing all items from the iterable in ascending order.

    This uses a custom implementation of mergesort that utilises a deque.
    final_length should not be input and is there to ensure the final deque 
    produced gets converted to a list.
    '''

    if not final_length:
        final_length = len(iterable)
    
    if len(iterable) <= 1:
        return iterable

    l1 = iterable[:len(iterable)//2]
    l2 = iterable[len(iterable)//2:]
    
    ml1 = mergesort(l1, final_length)
    ml2 = mergesort(l2, final_length)

    ml = amerge(ml1, ml2)

    return ml if len(ml) < final_length else list(ml)

def amerge(l1, l2):
    '''
    Return a sorted, merged deque of two input values or deques.
    '''
    l3 = deque()
    
    if len(l1) == 1:
        l1 = deque(l1)
    if len(l2) == 1:
        l2 = deque(l2)
    
    while l1 and l2:
        if l1[0] <= l2[0]:
            l3.append(l1.popleft())
        else:
            l3.append(l2.popleft())

    while l1 and not l2:
        l3.append(l1.popleft())

    while l2 and not l1:
        l3.append(l2.popleft())

    return l3

def altmergesort(mylist):
    '''
    Return a new list containing all items from the iterable in ascending order.
    This is an in-place version which relies on using pointers. It was created to
    reduce the space complexity to O(n) i.e. to use one common extra array for all merges.
    '''
    l = len(mylist)
    holdlist = [None] * l
    if l <= 1:
        return mylist
    else:
        submergesort(mylist,holdlist,0,l-1)
        return mylist

def submergesort(mylist,holdlist,left,right):

    if left == right:
        return (left,right)

    mid = (left + right) // 2

    ml1 = submergesort(mylist,holdlist,left=left,right=mid)
    ml2 = submergesort(mylist,holdlist,left=mid+1,right=right)

    ml = bmerge(mylist, holdlist, ml1, ml2)

    return ml

def bmerge(mylist, holdlist, l1, l2):

    # for i in range(l1[0], l1[1] + 1):
    #     holdlist[i] = mylist[i]

    holdlist[l1[0]:l1[1]+1] = mylist[l1[0]:l1[1]+1]

    l1curr = l1[0]
    l2curr = l2[0]
    curr = l1[0]

    while l1curr <= l1[1] and l2curr <= l2[1] and curr <= l2[1]:
        if holdlist[l1curr] <= mylist[l2curr]:
            mylist[curr] = holdlist[l1curr]
            l1curr += 1
            curr += 1
        else:
            mylist[curr] = mylist[l2curr]
            l2curr += 1
            curr += 1

    while l1curr <= l1[1] and curr <= l2[1]:
        mylist[curr] = holdlist[l1curr]
        l1curr += 1
        curr += 1

    return (l1[0], l2[1])