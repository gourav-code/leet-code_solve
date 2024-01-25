from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: [[int]]) -> int:
        if not grid:
            return 0

        maxArea = 0
        rows, cols = len(grid), len(grid[0])
        visit = set()

        def bsf(i, j):
            nonlocal maxArea
            visit.add((i, j))
            areatemp = 1
            q = deque()
            q.append((i, j))

            while q:
                r1, c1 = q.popleft()
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

                for rd, cd in directions:
                    r = r1 + rd
                    c = c1 + cd
                    if  (
                        r in range(rows) and c in range(cols)
                        and (r, c) not in visit and 
                        grid[r][c] == 1
                        ):
                        visit.add((r, c)) 
                        q.append((r, c))
                        areatemp += 1

            maxArea = max(maxArea, areatemp)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i, j) not in visit:
                    bsf(i, j)

        return maxArea

temp = Solution()
print(temp.maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]))