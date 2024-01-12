class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        #will use minHeap, min because to remove minimum element
        self.heap, self.k = nums, k
        heapq.heapify(self.heap)

        while( len(self.heap) > k):
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush( self.heap, val)

        if( len(self.heap) > self.k):
            heapq.heappop(self.heap)

        return self.heap[0]