class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ret = []
        hq = []
        for x,y in points:
            dist = math.sqrt(x**2 + y**2)
            heapq.heappush(hq,(dist,x,y))
        for i in range(k):
            dist, x,y = heapq.heappop(hq)
            ret.append([x,y])

        return ret