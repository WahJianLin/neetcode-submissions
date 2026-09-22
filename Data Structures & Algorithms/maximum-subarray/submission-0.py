class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ret = nums[0]
        cur = 0

        for i in range(len(nums)):
            cur = max(cur,0) + nums[i]
            ret = max(cur,ret)

        return ret