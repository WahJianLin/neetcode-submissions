class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ret = []
        arr = []
        total = 0
        numsLen = len(nums)
        def dfs(pos,total):
            if total == target:
                ret.append(arr.copy())
                return
            if total > target or pos >= numsLen:
                return
            val = nums[pos]
            arr.append(val)
            total += val
            dfs(pos, total)
            arr.pop()
            total -= val
            dfs(pos + 1, total)
        dfs(0, total)
        return ret