class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        ret = 0
        ROWS = len(grid)
        COLS = len(grid[0])

        visit = set()
        visit.add((0,0))
        queue = deque()
        queue.append((0,0))

        while queue:
            ret+=1
            for i in range(len(queue)):
                r,c = queue.popleft()
                if r == ROWS - 1 and c == COLS - 1:
                    return ret

                visit.add((r,c))
                n = [(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1),(0,1)]
                for nr, nc in n:
                    rr = r + nr
                    cc = c + nc
                    if rr < 0 or cc < 0 or rr == ROWS or cc == COLS or grid[rr][cc] == 1 or (rr,cc) in visit:
                        continue
                    queue.append((rr,cc))

        return -1