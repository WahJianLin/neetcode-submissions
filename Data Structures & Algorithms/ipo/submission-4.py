class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        mem = []
        hq = []
        for i in range(len(capital)):
            heapq.heappush(hq,(capital[i],-profits[i]))
        while k > 0:
            while hq and hq[0][0]<=w:
                curTup = heapq.heappop(hq)
                heapq.heappush(mem,curTup[1])
            if mem:
                w+=heapq.heappop(mem)*-1
            k-=1
        return w