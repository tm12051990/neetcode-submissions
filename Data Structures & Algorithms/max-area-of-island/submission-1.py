class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        currentMax = 0

        def dfs(r, c):
            count = 0
            if (min(r,c) < 0 or r == ROWS or c == COLS
                or grid[r][c] == 0 or (r,c) in visited):
                return 0

            visited.add((r,c))
            if grid[r][c] == 1:
                count += 1

            count += dfs(r + 1, c)
            count += dfs(r - 1, c)
            count += dfs(r, c + 1)
            count += dfs(r, c - 1)

            return count
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in visited and grid[r][c] == 1:
                    currentArea = dfs(r,c)
                    if currentArea > currentMax:
                        currentMax = currentArea
        return currentMax

        
