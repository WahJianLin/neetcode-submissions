class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ret = []
        cur = []
        nl = len(nums)
        def dfs(i, total):
            if total == target:
                ret.append(cur.copy())
                return
            if total>target or i >= nl:
                return
            val = nums[i]
            total += val
            cur.append(val)
            dfs(i,total)
            total -= val
            cur.pop()
            dfs(i+1,total)
        dfs(0,0)
        return ret