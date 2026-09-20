class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS = len(obstacleGrid)
        COLS = len(obstacleGrid[0])
        arr = [([0]*COLS) for _ in range(ROWS)]
        arr[ROWS-1][COLS-1] = 1 if obstacleGrid[ROWS-1][COLS-1] ==0 else 0
        def dp(r,c):
            # we don't need to worry about UP OR LEFT
            if r == ROWS or c == COLS or obstacleGrid[r][c] == 1:
                return 0
            if arr[r][c] != 0:
                return arr[r][c]
            arr[r][c] = dp(r+1,c) + dp(r,c+1)
            return arr[r][c]
        dp(0,0)
        
        return arr[0][0]