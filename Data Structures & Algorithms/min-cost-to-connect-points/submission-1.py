class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = {}
        for x,y in points:
            adj[(x,y)] = []

        for sx,sy in points:
            for ex, ey in points:
                if (sx,sy) != (ex,ey):
                    w = abs(sx - ex) + abs(sy - ey)
                    adj[(sx, sy)].append((w, (ex,ey)))
        
        ret = 0
        short = {}
        minH = [(0,(points[0][0], points[0][1]))]
        while minH:
            w, s = heapq.heappop(minH)
            if s in short:
                continue
            short[s] = w
            ret += w
            for aw, a in adj[s]:
                if a not in short:
                    heapq.heappush(minH, (aw,a))

        return ret