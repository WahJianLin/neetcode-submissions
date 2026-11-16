class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        nl = len(nums)
        memo = {}
        def dfs(i,a):
            if i == nl:
                return 1 if a == target else 0
            if (i,a) in memo:
                return memo[(i,a)]
            memo[(i,a)] = dfs(i+1,a-nums[i]) + dfs(i+1,a+nums[i])
            return memo[(i,a)]
            
        return dfs(0,0)