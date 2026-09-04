class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ret = 0
        ROWS = len(grid)
        COLS = len(grid[0])
        seen = set()
        nieghbors = [[1,0],[-1,0],[0,1],[0,-1]]

        def dfs(r,c): 
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r,c) in seen or grid[r][c] == "0":
                return
            seen.add((r,c))
            for nr, nc in nieghbors:
                rr = r + nr
                cc = c + nc
                dfs(rr,cc)

        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in seen and grid[r][c] != "0":
                    dfs(r,c)
                    ret+=1
                
        print(seen)

        return ret