class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        nl = len(nums)
        memo = {}
        
        def dfs(i, cur, ret):
            if (i, cur) in memo:
                return memo[(i,cur)]
            if i == nl:
                if cur == target:
                    ret+=1
                memo[(i,cur)] = ret
                return ret
            val = nums[i]
            memo[(i, cur)] = dfs(i+1, cur + val, ret) + dfs(i+1, cur - val, ret)
            return memo[(i, cur)]
        
        return dfs(0,0,0)