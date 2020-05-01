import random

def quicksort(iterable):
    '''
    Return a new list containing all items from the iterable in ascending order.

    This version takes the pivot to be the n//2th item in an iterable of length n+1.
    '''
    low = 0
    high = len(iterable)-1

    if high <= 0:
        return iterable

    return quicksorter(iterable,low,high)

def quicksortrand(iterable):
    '''
    Return a new list containing all items from the iterable in ascending order.

    This version takes the pivot to be a random item in the iterable.
    '''
    low = 0
    high = len(iterable)-1

    if high <= 0:
        return iterable

    return quicksorter(iterable,low,high,ptype='rand')


def quicksorter(iterable, low, high, ptype='mid'):
    if low >= high:
        return

    pivot = pivoter(iterable, low, high, ptype)

    quicksorter(iterable, low, pivot)
    
    quicksorter(iterable, pivot+1, high)
    
    return iterable

def pivoter(iterable, low, high, ptype='mid'):
    
    if ptype == 'mid':
        pivot = low + (high-low)//2
    elif ptype == 'rand':
        pivot = random.randint(low, high)

    i = low - 1

    for j in range(low, high+1):
        if j == pivot:
            pass
        elif iterable[j] <= iterable[pivot]:
            i += 1
            iterable[i], iterable[j] = iterable[j], iterable[i]
        else:
            pass

    return pivot