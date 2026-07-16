class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        target = len(nums)-k;
        heapq.heapify(nums)
        while target > 0:
            target -= 1
            heapq.heappop(nums)
        print(nums)
        return nums[0]