import heapq
class HeapSort:
    def sort(items):
        """ Heap sort using heapify """
        heapq.heapify(items)
        items[:] = [heapq.heappop(items) for i in range(len(items))]
