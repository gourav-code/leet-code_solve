class Solution:
    def swimInWater(self, grid: [[int]]) -> int:
        visit = set()
        n = len(grid)
        minHeap = [[grid[0][0], 0, 0]]
        direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while minHeap:
            t, r, c = heapq.heappop(minHeap)
            
            if r == n-1 and c == n-1:
                return t

            for l, b in direction:
                r1 = r + l
                c1 = c + b
                if (r1 not in range(n) or 
                    c1 not in range(n) or
                    (r1, c1) in visit):
                    continue
                visit.add((r1, c1))
                heapq.heappush(minHeap, [max(grid[r1][c1], t), r1, c1])
        