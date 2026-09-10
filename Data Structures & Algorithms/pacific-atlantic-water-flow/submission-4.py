class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ret = []

        rl = len(heights)
        cl = len(heights[0])
        pac = set()
        atl = set()
        neighbors = [[1,0],[-1,0],[0,1],[0,-1]]
        d = deque()

        def bfs(s,d):
            while d:
                for i in range(len(d)):
                    pr, pc = d.popleft()
                    for nr, nc in neighbors:
                        r = pr + nr
                        c = pc + nc
                        if r < 0 or c < 0 or r >= rl or c >= cl or (r,c) in s:
                            continue
                        orig = heights[pr][pc]
                        if orig <= heights[r][c]:
                            d.append((r,c))
                            s.add((r,c))

        for r in range(rl):
            d = deque()
            d.append((r,0))
            pac.add((r,0))
            bfs(pac, d)
            
            d = deque()
            d.append((r,cl-1))
            atl.add((r,cl-1))
            bfs(atl,d)
        for c in range(cl):
            d = deque()
            d.append((0,c))
            pac.add((0,c))
            bfs(pac, d)
            
            d = deque()
            d.append((rl-1,c))
            atl.add((rl-1,c))
            bfs(atl, d)
        for r in range(rl):
            for c in range(cl):
                if (r,c) in pac and (r,c) in atl:
                    ret.append([r,c])
        return ret