class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS = len(matrix)
        COLS = len(matrix[0])
        self.prefix = [[0] * COLS for _ in range(ROWS)]

        for r in range(ROWS):
            total = 0
            for c in range(COLS):
                total += matrix[r][c]
                self.prefix[r][c] = total

        for c in range(COLS):
            total = 0
            for r in range(ROWS):
                total += self.prefix[r][c]
                self.prefix[r][c] = total


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        total = self.prefix[row2][col2]
        above = self.prefix[row1 - 1][col2] if row1 > 0 else 0
        left = self.prefix[row2][col1 - 1] if col1 > 0 else 0
        overlap = self.prefix[row1 - 1][col1 - 1] if row1 > 0 and col1 > 0 else 0

        return ((total - above - left) + overlap)


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)