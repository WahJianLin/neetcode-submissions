class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rl = len(grid)
        cl = len(grid[0])
        seen = set()
        maxArea = 0
        def dfs(r,c):
            if r < 0 or c < 0 or r == rl or c == cl or (r, c) in seen or grid[r][c] == 0:
                return 0
            seen.add((r,c))
            t = 1
            
            t+=dfs(r+1,c)
            t+=dfs(r-1,c)
            t+=dfs(r,c+1)
            t+=dfs(r,c-1)

            return t

        for i in range(rl):
            for j in range(cl):
                if grid[i][j] == 1 and (i,j) not in seen:
                    area = dfs(i,j)
                    maxArea = max(maxArea, area)
        return maxArea