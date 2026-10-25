class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        # create adj list
        neighbors = [[1,0],[-1,0],[0,1],[0,-1]]
        adj = {}
        for r  in range(ROWS):
            for c in range(COLS):
                aList = adj.get((r,c),[])
                for nr, nc in neighbors:
                    rr = r + nr
                    cc = c + nc
                    if rr < 0 or rr >= ROWS or cc < 0 or cc >= COLS:
                        continue
                    aList.append((rr,cc))
                adj[(r,c)] = aList
                
        short={}
        h = [(grid[0][0],(0,0))] #puts the starting location
        while h:
            w, coord = heapq.heappop(h)
            coordR,coordC = coord

            if (coordR,coordC) in short:
                continue
            short[coord] = w

            coordVal = grid[coordR][coordC]
            for r,c in adj[coord]:
                if (r,c) in short:
                    continue
                gVal = grid[r][c]
                calcW = w if w > gVal else gVal
                heapq.heappush(h,(calcW,(r,c)))


        print(short)
        return short[(ROWS-1,COLS-1)]