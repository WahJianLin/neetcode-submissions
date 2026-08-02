class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rl = len(grid)
        cl = len(grid[0])
        fruits = 0
        time = -1
        seen =  set()
        d = deque()
        adj = [[1,0], [-1,0], [0,1], [0,-1]]
        

        for i in range(rl):
            for j in range(cl):
                val = grid[i][j]
                if val == 0:
                    seen.add((i,j))
                if val == 1:
                    fruits += 1
                if val == 2:
                    seen.add((i,j))
                    d.append((i,j))
        
        if fruits == 0:
            return 0
        while d:
            for i in range(len(d)):
                r,c = d.popleft()
                    
                for ar, ac in adj:
                    rr = r + ar
                    cc = c + ac
                    if rr < 0 or cc < 0 or rr == rl or cc == cl or (rr,cc) in seen:
                        continue
                    fruits -= 1
    
                    seen.add((rr,cc))
                    d.append((rr,cc))
            time+=1
        print(fruits)
        return -1 if fruits > 0 else time