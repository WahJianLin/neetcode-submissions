class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS = len(obstacleGrid)
        COLS = len(obstacleGrid[0])
        arr = [(COLS* [-1]) for _ in range(ROWS)]
        if ROWS == 1 and COLS == 1:
            ogVal = obstacleGrid[0][0]
            return 1 if ogVal == 0 else 0
        if obstacleGrid[ROWS-1][COLS-1] == 1:
            return 0
        arr[ROWS-1][COLS-1]=1
        
        def dp(r,c):
            if r < 0 or c < 0 or r == ROWS or c == COLS:
                return 0
            if obstacleGrid[r][c] == 1:
                arr[r][c] = 0
                return 0 
            val = 0
            if r+1 < ROWS:
                rVal = arr[r+1][c]
                if rVal != -1:
                    val += rVal
                else:
                    val += dp(r+1,c)
            if c+1 < COLS:
                cVal = arr[r][c+1]
                if cVal != -1:
                    val += arr[r][c+1]
                else:
                    val += dp(r,c+1)
            arr[r][c] = val
            return val
        dp(0,0)
        
        return arr[0][0]