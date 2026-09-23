class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        nl = len(nums)
        gMax = nums[0]
        gMin = nums[0]
        curMax = 0
        curMin = 0
        total = 0

        for i in range(nl):
            total += nums[i]
            curMax = max(curMax, 0) + nums[i]
            gMax = max(curMax,gMax)
            curMin = min(curMin, 0) + nums[i]
            gMin = min(curMin,gMin)
        print(gMax)
        if gMax < 0:
            return gMax
        return max(gMax, (total - gMin))