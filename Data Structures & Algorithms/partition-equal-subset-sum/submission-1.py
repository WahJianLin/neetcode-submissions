class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nl = len(nums)
        total = sum(nums)/2
        memo = {}
        def dfs(i, s1):
            if (i,s1) in memo:
                return memo[(i,s1)]
            if s1 > total:
                return False
            if i == nl:
                return s1 == total
            memo[(i+1), s1] = dfs(i+1, s1)
            memo[(i+1), s1+nums[i]] = dfs(i+1, s1+nums[i])
            return memo[(i+1), s1] or memo[(i+1), s1+nums[i]]
        return dfs(0,0)