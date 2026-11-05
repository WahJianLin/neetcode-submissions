class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        nl = len(nums)
        memo ={}
        def dfs(i, total):
            if i == nl:
                return 1 if total == target else 0

            if (i,total) in memo:
                return memo[(i,total)]
            memo[(i+1, total - nums[i])] = dfs(i+1, total - nums[i])
            memo[(i+1, total + nums[i])] = dfs(i+1, total + nums[i])

            return memo[(i+1, total - nums[i])] + memo[(i+1, total + nums[i])]

        return dfs(0, 0)