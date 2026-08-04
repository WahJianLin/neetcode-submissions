class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # should be a bfs because we are trying to get the nearest thing trasure to land

        rl = len(grid)
        cl = len(grid[0])
        seen = set() #check if we need this. we might not
        d = deque()
        adj = [[1,0],[-1,0],[0,1],[0,-1]]

        dist = 1
        # look for all treasure
        # idea is to look for land from the treasure point of view. like a sonar from each treasure

        for i in range(rl):
            for j in range(cl):
                val = grid[i][j]
                if val == 0:
                    d.append((i,j))
                    seen.add((i,j))
                if val == -1:
                    seen.add((i,j))

        while d:
            for i in range(len(d)):
                r, c = d.popleft()
                for ar, ac  in adj:
                    rr = r + ar
                    cc = c + ac

                    if rr < 0 or cc < 0 or rr == rl or cc == cl or (rr,cc) in seen:
                        continue
                    
                    val = grid[rr][cc]
                    if dist < val:
                        grid[rr][cc] = dist
                        d.append((rr,cc))
            dist+=1


