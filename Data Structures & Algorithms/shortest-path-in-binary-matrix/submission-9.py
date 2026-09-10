class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rl = len(grid)
        cl = len(grid[0]) 
        seen = set()
        d = deque()
        if grid[0][0]!=1:
            d.append((0,0))
        neighbors = [[1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1]]
        step = 1

        while d:
            for i in range(len(d)):
                r,c = d.popleft()
                print(r,c)
                if r == rl -1  and c == cl -1:
                    return step
                for nr, nc in neighbors:
                    rr = r + nr
                    cc = c + nc
                    
                    if rr < 0 or cc < 0 or rr >= rl or cc >= cl or (rr,cc) in seen or grid[rr][cc] ==1:
                        continue

                    d.append((rr,cc))
                    seen.add((rr,cc))
                
            step+=1
                    
                    

        return -1