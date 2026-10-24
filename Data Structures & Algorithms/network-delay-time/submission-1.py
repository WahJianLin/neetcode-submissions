class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}
        ret = -1
        for i in range(1,n+1):
            adj[i] = []

        for ui, vi, ti in times:
            adj[ui].append((vi,ti))

        short = {}
        minH = [(0, k)]
        while minH:
            w, v = heapq.heappop(minH)
            if v in short:
                continue
            short[v] = w
            ret = max(ret,w)
            print(ret)
            
            for av, aw in adj[v]:
                if av not in short:
                    heapq.heappush(minH,(aw+w, av))

        return ret if len(short) == n else -1