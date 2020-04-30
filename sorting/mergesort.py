from collections import deque

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

# TODO: fix alt version to work without creating new lists/deques

# def altmergesort(mylist):
#     l = len(mylist)
#     return mylist if l <= 1 else submergesort(mylist,0,l-1, l)

# def submergesort(mylist, left,right, final_length=False):
#     if not final_length:
#         final_length = len(mylist)

#     if left == right:
#         return mylist[left]

#     mid = (left + right) // 2

#     ml1 = submergesort(mylist, left=left, right=mid, final_length=final_length)
#     ml2 = submergesort(mylist, left=mid+1, right=right, final_length=final_length)

#     ml = bmerge(ml1, ml2)

#     return ml if len(ml) < final_length else list(ml)

# def bmerge(l1, l2):
#     '''
#     Return a sorted, merged deque of two input values or deques.
#     '''
#     l3 = deque()

#     if isinstance(l1, int):
#         l1 = deque([l1])
#     if isinstance(l2, int):
#         l2 = deque([l2])

#     while l1 and l2:
#         if l1[0] < l2[0]:
#             l3.append(l1.popleft())
#         else:
#             l3.append(l2.popleft())

#     while l1 and not l2:
#         l3.append(l1.popleft())

#     while l2 and not l1:
#         l3.append(l2.popleft())

#     return l3