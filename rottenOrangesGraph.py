class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time, fresh = 0, 0
        rows, cols = len(grid), len(grid[0])
        q = deque()

        def rotten(r, c, q, fresh):
            if ( r not in range(rows) or
                c not in range(cols) or
                grid[r][c] != 1):
                return fresh

            grid[r][c] = 2
            q.append((r, c))
            fresh -= 1
            return fresh

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))


        while q and fresh > 0:
            for tmp in range(len(q)):
                r, c = q.popleft()
                temp = rotten(r, c + 1, q, fresh)
                temp = rotten(r + 1, c, q, temp)
                temp = rotten(r, c - 1, q, temp)
                temp = rotten(r - 1, c, q, temp)
                fresh = temp
            time += 1

        return time if fresh == 0 else -1
