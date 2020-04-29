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

    ml = merge(ml1, ml2)

    return ml if len(ml) < final_length else list(ml)

def merge(l1, l2):
    '''
    Return a sorted, merged deque of two input values or deques.
    '''
    l3 = deque()
    
    if len(l1) == 1:
        l1 = deque(l1)
    if len(l2) == 1:
        l2 = deque(l2)
    
    while l1 and l2:
        if l1[0] < l2[0]:
            l3.append(l1.popleft())
        else:
            l3.append(l2.popleft())

    while l1 and not l2:
        l3.append(l1.popleft())

    while l2 and not l1:
        l3.append(l2.popleft())

    return l3