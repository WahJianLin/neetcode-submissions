class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        for i in range(len(nums)-k):
            val = heapq.heappop(nums)
        return heapq.heappop(nums)