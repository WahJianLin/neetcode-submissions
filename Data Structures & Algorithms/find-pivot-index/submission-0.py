class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        nl = len(nums)
        prefix = [nums[0]] * nl
        suffix = [nums[nl-1]] * nl
        for i in range(1,nl):
            prefix[i] = prefix[i-1] + nums[i]
        for j in range(nl - 2, -1, -1):
            suffix[j] = suffix[j+1] + nums[j]
        for t in range(nl):
            if prefix[t] == suffix[t]:
                return t

        return -1