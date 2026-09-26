class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        nl = len(nums)
        ret = nl+1
        total = 0

        for r in range(nl):
            total += nums[r]
            while total >= target:
                ret = min(ret, r-l +1)
                total -= nums[l]
                l+=1

        return 0 if ret == nl+1 else ret