class KthLargest:
    h = []
    size = 0
    def __init__(self, k: int, nums: List[int]):
        self.h = nums
        self.size = k
        heapq.heapify(self.h)
        numLen = len(nums) - k
        while len(nums) > k:
            heapq.heappop(self.h)

    def add(self, val: int) -> int:
        heapq.heappush(self.h, val)
        if len(self.h) > self.size:
            heapq.heappop(self.h)
        return self.h[0]
