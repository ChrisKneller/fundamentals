def quicksort(iterable):
    '''
    Return a new list containing all items from the iterable in ascending order.

    This version takes the pivot to be the n//2th item in a string of length n+1.
    '''
    low = 0
    high = len(iterable)-1

    if high <= 0:
        return iterable

    return quicksorter(iterable,low,high)

def quicksorter(iterable, low, high):
    if low >= high:
        return

    pivot = pivoter(iterable, low, high)

    quicksorter(iterable, low, pivot)
    
    quicksorter(iterable, pivot+1, high)
    
    return iterable

def pivoter(iterable, low, high):
    
    pivot = low + (high-low)//2

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