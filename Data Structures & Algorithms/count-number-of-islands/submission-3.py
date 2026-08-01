class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rl = len(grid)
        cl = len(grid[0])
        seen = set()
        islands = 0
        def dfs(r,c):
            if r < 0 or c < 0 or r == rl or c == cl or (r,c) in seen or grid[r][c] == '0':
                return
            seen.add((r,c))
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        for i in range(rl):
            for j in range(cl):
                if grid[i][j] == "1" and (i,j) not in seen:
                    dfs(i,j)
                    islands +=1
        return islands