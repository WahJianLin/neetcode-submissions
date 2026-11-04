class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        nl = len(nums)
        memo = {}
        
        def dfs(i, cur):
            if i == nl:
                if cur == target:
                    return 1
                return 0
            
            if (i, cur) in memo:
                return memo[(i,cur)]
            val = nums[i]
            memo[(i, cur)] = dfs(i+1, cur + val) + dfs(i+1, cur - val)
            return memo[(i, cur)]
        
        return dfs(0,0)