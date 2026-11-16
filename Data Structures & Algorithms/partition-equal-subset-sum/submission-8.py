class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        total = sum(nums)
        if total % 2 == 1:
            return False

        nl = len(nums)
        target = total // 2 # the value that signifies equality

        memo = {}
        def dfs(i,t):
            if t == 0:
                return True
            if i == nl or t < 0:
                return False
            if (i,t) in memo:
                return memo[(i,t)]
            memo[(i,t)] = dfs(i+1,t) or dfs(i+1,t - nums[i])
            return memo[(i,t)]


        return dfs(0,target)