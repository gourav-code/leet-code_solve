class Solution:
    def numIslands(self, grid: [[str]]) -> int:
        if not grid:
            return 0

        numIsland = 0
        visit = set()
        rows, cols = len(grid), len(grid[0])

        def bfs(r, c):
            visit.add((r, c))
            q = deque()
            q.append((r, c))

            while q:
                r1, c1 = q.popleft()
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

                for rd, cd in directions:
                    r = r1 + rd
                    c = c1 + cd
                    if (
                       r in range(rows) and
                       c in range(cols) and
                       (r, c) not in visit and
                       grid[r][c] == "1"
                       ):
                       visit.add((r, c))
                       q.append((r, c))


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    numIsland += 1
        
        return numIsland