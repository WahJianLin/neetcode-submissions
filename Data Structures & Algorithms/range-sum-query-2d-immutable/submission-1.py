class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS = len(matrix)
        COLS = len(matrix[0])
        self.prefix = [(COLS*[0]) for i in range(ROWS)]
        self.prefix[0][0] = matrix[0][0]
        for r in range(1,ROWS):
            self.prefix[r][0] = self.prefix[r-1][0] + matrix[r][0]
            
        for c in range(1,COLS):
            self.prefix[0][c] = self.prefix[0][c-1] + matrix[0][c]
        
        for r in range(1,ROWS):
            for c in range(1,COLS):
                self.prefix[r][c] = self.prefix[r-1][c] + self.prefix[r][c-1] + matrix[r][c] - self.prefix[r-1][c-1]
        print(self.prefix)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        topRect = 0 if row1 == 0 else self.prefix[row1-1][col2] 
        leftRect = 0 if col1 == 0 else self.prefix[row2][col1-1]
        corner = 0 if row1 == 0 or col1 == 0 else self.prefix[row1-1][col1-1]
        removeArea = topRect + leftRect - corner
        return self.prefix[row2][col2] - removeArea
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)