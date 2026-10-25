class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = {}
        for i in range(n):
            adj[i] = []
        for j in range(len(edges)):
            s,e = edges[j]
            w = succProb[j]
            adj[s].append((w,e))
            adj[e].append((w,s))
        djMap = {}
        h = [(-1,start_node)]

        while h:
            popW, popV = heapq.heappop(h)
            
            if popV in djMap:
                continue
            popW*=-1
            djMap[popV] = popW

            for w, e in adj[popV]:
                if e not in djMap:
                    newW = -1 * w *popW
                    heapq.heappush(h,(newW,e))
        return djMap[end_node] if end_node in djMap else 0