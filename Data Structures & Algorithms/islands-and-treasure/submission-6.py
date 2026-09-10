class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rl = len(grid)
        cl = len(grid[0])
        d = deque()
        seen = set()
        neighbors = [[1,0],[-1,0],[0,1],[0,-1]]
        step = 0
        for r in range(rl):
            for c in range(cl):
                val = grid[r][c]
                if val == 0:
                    d.append((r,c))
                    seen.add((r,c))
                if val == -1:
                    seen.add((r,c))
        
        while d:
            for i in range(len(d)):
                r,c = d.popleft()
                grid[r][c] = step
                for nr, nc in neighbors:
                    rr = r + nr
                    cc = c + nc
                    if rr < 0 or cc < 0 or rr >= rl or cc >= cl or (rr,cc) in seen:
                        continue
                    seen.add((rr,cc))
                    d.append((rr,cc))
            step+=1