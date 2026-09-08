class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ret = 0 
        ROWS = len(grid)
        COLS = len(grid[0])
        seen = set()
        neighbors = [[1,0],[-1,0],[0,1],[0,-1]]
        
        def dfs(r,c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r,c) in seen or grid[r][c] == 0:
                return 0
            seen.add((r,c))
            total=1
            for nr, nc in neighbors:
                rr = r + nr
                cc = c + nc
                total += dfs(rr,cc)

            return total
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1 and (i,j) not in seen:
                    area = dfs(i,j)
                    ret = max(ret, area)
        return ret 