class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ret = []
        l = []
        for p in points:
            dist = (p[0]**2) +(p[1]**2)
            l.append((dist, p[0], p[1]))
        heapq.heapify(l)
        mini = l[0][0]
        

        while k:
            val = heapq.heappop(l)
            ret.append([val[1],val[2]])
            k-=1

        return ret