class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        islands = 0
        def dfs(r, c):
            if (min(r, c) < 0 or r == ROWS or c == COLS
                or (r, c) in visit):
                return

            if (grid[r][c] == "0"):
                return

            visit.add((r,c))

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for i in range(ROWS):
            for j in range(COLS):
                if (i,j) not in visit and grid[i][j] == "1":
                    islands += 1
                    dfs(i, j)
        return islands




