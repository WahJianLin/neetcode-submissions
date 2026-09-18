class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS = len(obstacleGrid)
        COLS = len(obstacleGrid[0])
        
        if obstacleGrid[ROWS-1][COLS-1] == 1:
            return 0

        bot = [0] * COLS
        bot[COLS-1] = 1

        for r in range(ROWS-1,-1,-1):
            
            top = [0] * COLS
            top[COLS-1] = 0 if bot[COLS-1] == 0 or obstacleGrid[r][COLS-1] == 1 else 1
            for c in range(COLS-2,-1,-1):
                if obstacleGrid[r][c] == 1:
                    top[c] = 0
                    continue
                top[c] = bot[c] + top[c+1]
            bot = top
            
        return bot[0]