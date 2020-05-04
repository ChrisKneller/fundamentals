import heapq

def heapsort_a(iterable):
    '''
    Return a new list containing all items from the iterable in ascending order.

    This utilises Python's built in heap.
    '''
    heapq.heapify(iterable)
    return [heapq.heappop(iterable) for i in range(len(iterable))]

# def heapsort_b(iterable):


class maxHeap():
    def __init__(self, heap=None):
        self.heap = [] if heap is None else heap

    def insert(self, value):
        self.heap.append(value)
        self.bubble_up(len(self.heap)-1)

    def show(self):
        return self.heap

    def bubble_up(self, child_index):
        parent_index = child_index//2
        while self.heap[child_index] > self.heap[parent_index]:
            self.heap[child_index], self.heap[parent_index] = self.heap[parent_index], self.heap[child_index]
            child_index = parent_index
            parent_index = child_index//2