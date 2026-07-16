class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ret = 0
        fresh = 0
        ROWS = len(grid)
        COLS = len(grid[0])

        visit = set()
        queue = deque()

        
        n = [(1,0),(-1,0),(0,1),(0,-1)]

        for r in range(ROWS):
            for c in range(COLS):
                val = grid[r][c]
                if val == 0:
                    visit.add((r,c))
                elif val == 1:
                    fresh+=1
                else:
                    visit.add((r,c))
                    queue.append((r,c))
        
        if fresh <= 0:
            return ret
        while queue:
            ret +=1
            for i in range(len(queue)):
                r,c = queue.popleft()

                visit.add((r,c))

                for nr, nc in n:
                    rr = r + nr
                    cc = c + nc

                    if rr < 0 or cc < 0 or rr == ROWS or cc == COLS or (rr,cc) in visit or (rr,cc) in queue:
                        continue
                    fresh -= 1
                    queue.append((rr,cc))
            if fresh <= 0:
                return ret

        return -1
