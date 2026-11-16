class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        total = sum(nums)
        if total % 2 == 1:
            return False

        nl = len(nums)
        target = total // 2 # the value that signifies equality

        memo = {}
        def dfs(i,t):
            if (i,t) in memo:
                return memo[(i,t)]
            if i == nl:
                return False
            if t == 0:
                return True
            memo[(i+1,t)] = dfs(i+1,t)
            memo[(i+1,t - nums[i])] = dfs(i+1,t - nums[i])
            return  memo[(i+1,t)] or memo[(i+1,t - nums[i])]


        return dfs(0,target)