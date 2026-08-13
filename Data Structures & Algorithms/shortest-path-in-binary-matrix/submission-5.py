class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        queue = deque()
        queue.append((0,0))
        visited.add((0,0))
        length = 1

        if grid[0][0] == 1:
            return -1

        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                if r == ROWS - 1 and c == COLS - 1:
                    return length

                neighbors = [[0,1],[1,0],[-1,0],[0,-1],[1,1],[-1,-1],[-1,1],[1,-1]]

                for dr, dc in neighbors:
                    if (min(dr + r, dc + c) < 0 or r + dr == ROWS or c + dc == COLS
                        or (dr + r, dc + c) in visited or grid[dr + r][dc + c] == 1):
                        continue
                    queue.append((r + dr, c + dc))
                    visited.add((r + dr, c + dc))
            length += 1

        return -1

