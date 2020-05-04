import random

def quicksort(iterable):
    '''
    Return a new list containing all items from the iterable in ascending order.

    This version takes the pivot to be the last item in an iterable.
    '''
    low = 0
    high = len(iterable)-1

    if high <= 0:
        return iterable

    return quicksorter(iterable,low,high)

def quicksorter(iterable, low, high, ptype='hi'):
    if low >= high:
        return

    pivot = pivoter(iterable, low, high, ptype)

    quicksorter(iterable, low, pivot-1)
    
    quicksorter(iterable, pivot+1, high)
    
    return iterable

def pivoter(iterable, low, high, ptype='hi'):
    
    if ptype == 'hi':
        pivot = high

    pivot_number = iterable[pivot]

    i = low - 1

    for j in range(low, high):
        if iterable[j] <= pivot_number:
            i += 1
            iterable[i], iterable[j] = iterable[j], iterable[i]
        else:
            pass
    
    i += 1

    iterable[i], iterable[high] = iterable[high], iterable[i]

    return i