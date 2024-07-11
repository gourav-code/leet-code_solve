from collections import deque, defaultdict
from typing import List, Tuple

class Solution:
    def MaxConnection(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        row, col = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def bfs(r, c, comp_id):
            queue = deque([(r, c)])
            visited.add((r, c))
            size = 1
            components[r][c] = comp_id
            while queue:
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < row and 0 <= ny < col and grid[nx][ny] == 1 and (nx, ny) not in visited:
                        visited.add((nx, ny))
                        queue.append((nx, ny))
                        size += 1
                        components[nx][ny] = comp_id
            return size
        
        visited = set()
        components = [[-1] * col for _ in range(row)]
        comp_sizes = []
        comp_id = 0
        
        # Step 1: Identify all connected components of 1's
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1 and (r, c) not in visited:
                    size = bfs(r, c, comp_id)
                    comp_sizes.append(size)
                    comp_id += 1
        
        # Step 2: Calculate the maximum size by changing one 0 to 1
        max_size = max(comp_sizes) if comp_sizes else 0
        
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 0:
                    seen_comps = set()
                    new_size = 1
                    for dx, dy in directions:
                        nx, ny = r + dx, c + dy
                        if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1:
                            comp_idx = components[nx][ny]
                            if comp_idx not in seen_comps:
                                new_size += comp_sizes[comp_idx]
                                seen_comps.add(comp_idx)
                    max_size = max(max_size, new_size)
        
        return max_size

# Example usage
grid = [
    [1, 0, 0, 1],
    [1, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 0, 1]
]

sol = Solution()
print(sol.MaxConnection(grid))  # Output: 7
