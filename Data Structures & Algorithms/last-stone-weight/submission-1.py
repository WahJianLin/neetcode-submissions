class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            diff = x-y
            if diff != 0:
                heapq.heappush(stones, diff)

        return abs(heapq.heappop(stones)) if stones else 0