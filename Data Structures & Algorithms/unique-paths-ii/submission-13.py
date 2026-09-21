class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS = len(obstacleGrid)
        COLS = len(obstacleGrid[0])
        bot = [0] * COLS
        rOpen = True

        for r in range(ROWS-1 ,-1, -1):
            top = [0] * COLS
            if obstacleGrid[r][COLS-1] == 1:
                rOpen = False
            if rOpen:
                top[COLS-1] = 1
            for c in range(COLS - 2, -1, -1):
                if obstacleGrid[r][c] == 1:
                    top[c] = 0
                else:
                    top[c] = bot[c] + top[c+1]
            bot = top
            print(top)
        
        return bot[0]