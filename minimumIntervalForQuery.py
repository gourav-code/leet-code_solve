class Solution:
    def minInterval(self, intervals: [[int]], queries: [int]) -> [int]:

        intervals.sort()
        minHeap = []
        output,i = {},0
        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                l,r = intervals[i]
                heapq.heappush(minHeap, (r-l+1,r))
                i+=1

            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
            
            output[q] = minHeap[0][0] if minHeap else -1

        ans = [output[q] for q in queries]

        return ans

        