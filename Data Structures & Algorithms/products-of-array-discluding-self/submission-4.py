class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nl = len(nums)
        prefix = [nums[0]] * nl
        suffix = [nums[nl-1]] * nl
        ret = [0]*nl

        for i in range(1, nl):
            prefix[i] = prefix[i-1] * nums[i]

        for j in range(nl-2, -1, -1):
            suffix[j] = suffix[j+1] * nums[j]

        for k in range(nl):
            pre = 1 if k == 0 else prefix[k-1]
            suf = 1 if k == nl - 1 else suffix[k+1]
            ret [k] = pre * suf
        return ret

