class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ret = []

        rl = len(heights)
        cl = len(heights[0])
        pac = set()
        atl = set()
        nieghbors = [[1,0],[-1,0],[0,1],[0,-1]]

        def dfs(r,c,s):
            if r < 0 or c < 0 or r >= rl or c >= cl or (r,c) in s:
                return
            s.add((r,c))
            for nr, nc in nieghbors:
                orig = heights[r][c]
                rr = r + nr
                cc = c + nc
                if rr < 0 or cc < 0 or rr >= rl or cc >= cl or orig <= heights[rr][cc]:
                    dfs(rr,cc,s)
        for r in range(rl):
            dfs(r,0,pac)
            dfs(r,cl-1,atl)
        for c in range(cl):
            dfs(0,c,pac)
            dfs(rl-1,c,atl)
        
        for r in range(rl):
            for c in range(cl):
                if (r,c) in pac and (r,c) in atl:
                    ret.append([r,c])
        return ret