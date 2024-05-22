class Solution:
    def islandsAndTreasure(self, grid: [[int]]) -> None:
        visit = set()
        m = len(grid)
        n = len(grid[0])
        q = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append([i,j])
                    visit.add((i,j))

        def helper(r,c):
            if( (r,c) in visit or
            r not in range(m) or 
            c not in range(n) or
            grid[r][c] == -1
            ):
                return 
            q.append([r,c])
            visit.add((r,c))

        distance = 0
        while q:
            for i in range(len(q)):
                r,c  = q.popleft()
                grid[r][c] = distance
                helper(r+1,c)
                helper(r,c+1)
                helper(r,c-1)
                helper(r-1,c)
            distance += 1
