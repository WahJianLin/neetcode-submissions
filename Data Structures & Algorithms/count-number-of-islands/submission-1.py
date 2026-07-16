class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        visit = set()
        count = 0

        def dfs(r,c):
            if r < 0 or c < 0 or r == ROWS or c == COLS or (r,c) in visit or grid[r][c] == "0":
                return
            visit.add((r,c))
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
            return

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r,c) not in visit:
                    count+=1
                    dfs(r,c)
                visit.add((r,c))
        

            
        return count
        