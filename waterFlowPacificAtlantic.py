class Solution:
    def pacificAtlantic(self, heights: [[int]]) -> [[int]]:
        rows, cols = len(heights), len(heights[0])

        result = []
        pacificVisit, atlanticVisit = set(), set()

        def dfs(r, c, visit, prevHeight):
            if (r not in range(rows) or
                c not in range(cols) or
                (r, c) in visit or prevHeight > heights[r][c]):
                return

            visit.add((r, c))
            dfs(r+1, c, visit, heights[r][c])
            dfs(r, c+1, visit, heights[r][c])
            dfs(r, c-1, visit, heights[r][c])
            dfs(r-1, c, visit, heights[r][c])


        for c in range(cols):
            dfs(0, c, pacificVisit, heights[0][c])
            dfs(rows-1, c, atlanticVisit, heights[rows-1][c])

        for r in range(rows):
            dfs(r, 0, pacificVisit, heights[r][0])
            dfs(r, cols-1, atlanticVisit, heights[r][cols-1])


        for r in range(rows):
            for c in range(cols):
                if (r, c) in atlanticVisit and (r, c) in pacificVisit:
                    result.append([r, c])

        return result