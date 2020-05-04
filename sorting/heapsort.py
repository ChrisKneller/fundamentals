import heapq


def heapsort_a(iterable):
    '''
    Return a new list containing all items from the iterable in ascending order.

    This utilises Python's built in heap.
    '''
    heapq.heapify(iterable)
    return [heapq.heappop(iterable) for _ in range(len(iterable))]


# Oh no... why did I build a maxHeap class instead of a minHeap class? 
# Now I have to reverse the final list or build a minHeap class from scratch!
# TODO: build a minHeap class and save reversing the list at the end
def heapsort_b(iterable):
    '''
    Return a new list containing all items from the iterable in ascending order.

    This utilises a custom maxHeap class.
    '''
    myheap = maxHeap(iterable)
    myheap.heapify()
    return [myheap.pop() for _ in range(len(iterable))][::-1]


class maxHeap():
    def __init__(self, heap=None):
        self.heap = [] if heap is None else heap

    def insert(self, value):
        self.heap.append(value)
        self.bubble_up(len(self.heap)-1)

    def show(self):
        return self.heap

    def bubble_up(self, child_index):
        while child_index > 0:
            parent_index = (child_index-1)//2
            if self.heap[child_index] > self.heap[parent_index]:
                self.heap[child_index], self.heap[parent_index] = self.heap[parent_index], self.heap[child_index]
                child_index = parent_index
            else:
                return

    def bubble_down(self, parent_index):
        while parent_index < len(self.heap) - 1:
            max_child_index = self.get_max_child_index(parent_index)
            if not max_child_index:
                return
            if self.heap[parent_index] < self.heap[max_child_index]:
                self.heap[parent_index], self.heap[max_child_index] = self.heap[max_child_index], self.heap[parent_index]
                parent_index = max_child_index
            else:
                return

    def get_max_child_index(self, parent_index):
        lchild_index = parent_index * 2 + 1
        rchild_index = (parent_index + 1) * 2
        if lchild_index > len(self.heap) - 1:
            return None
        elif rchild_index > len(self.heap) - 1:
            return lchild_index
        else:
            return lchild_index if self.heap[lchild_index] >= self.heap[rchild_index] else rchild_index

    def heapify(self, parent_index=False):
        if parent_index == False:
            for i in range(len(self.heap)-1,0,-1):
                parent_index = (i-1)//2
                max_child_index = self.get_max_child_index(parent_index)
                if self.heap[max_child_index] > self.heap[parent_index]:
                    self.heap[max_child_index], self.heap[parent_index] = self.heap[parent_index], self.heap[max_child_index]
                self.heapify(max_child_index)
        else:
            max_child_index = self.get_max_child_index(parent_index)
            if not max_child_index:
                return
            if self.heap[max_child_index] > self.heap[parent_index]:
                self.heap[max_child_index], self.heap[parent_index] = self.heap[parent_index], self.heap[max_child_index]
            self.heapify(max_child_index)

    def peek(self):
        return self.heap[0]

    def pop(self):
        highest = self.heap[0]
        self.heap[0] = self.heap[len(self.heap) - 1]
        self.heap.pop()
        self.bubble_down(0)
        return highest

def is_max_heap(heap: list, i: int, n: int) -> bool:
    '''
    Return a boolean value stating if the input list is a max heap.

        Keyword arguments:
            heap -- your input heap
            i -- the index of the first value in the heap (0)
            n -- the index of the last value in the heap (len(heap) - 1)
    '''
    if i > int((n-2)/2):
        return True

    if(heap[i] >= heap[2*i+1] and
       heap[i] >= heap[2*i+2] and
       is_max_heap(heap, 2*i+1,n) and
       is_max_heap(heap, 2*i+2,n)):
        return True

    return False
