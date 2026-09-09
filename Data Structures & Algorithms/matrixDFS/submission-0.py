class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        ret = 0
        rl = len(grid)
        cl = len(grid[0])
        neighbors = [[1,0],[-1,0],[0,1],[0,-1]]

        seen = set()

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rl or c >= cl or (r,c) in seen or grid[r][c] == 1:
                return 0
            if r == rl-1 and c == cl-1:
                print('hi')
                return 1
            seen.add((r,c))
            ret = 0
            for nr, nc in neighbors:
                rr = r + nr
                cc = c + nc
                ret += dfs(rr,cc)
            seen.remove((r,c))
            return ret
        return dfs(0,0)
