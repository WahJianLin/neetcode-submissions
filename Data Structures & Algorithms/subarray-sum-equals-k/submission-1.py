class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        nl = len(nums)
        prefix = [0] * nl
        prefix[0] = nums[0]
        ret = 0

        for i in range(1,nl):
            prefix[i] = prefix[i-1] + nums[i]
        l = -1
        rem = 0
        m = {}
        m[0] = 1
        for r in range(nl):
            val = prefix[r]
            diff = val - k
            ret += m.get(diff,0)
            m[val] = m.get(val,0) + 1
        return ret