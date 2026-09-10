class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rl = len(grid)
        cl = len(grid[0]) 
        seen = set()
        d = deque()
        d.append((0,0))
        neighbors = [[1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1]]
        step = 1

        while d:
            for i in range(len(d)):
                r,c = d.popleft()
                if r < 0 or c < 0 or r >= rl or c >= cl or (r,c) in seen or grid[r][c] ==1:
                    continue
                seen.add((r,c))
                print(r,c)
                if r == rl -1  and c == cl -1:
                    return step
                for nr, nc in neighbors:
                    rr = r + nr
                    cc = c + nc
                    d.append((rr,cc))
                
            step+=1
                    
                    

        return -1