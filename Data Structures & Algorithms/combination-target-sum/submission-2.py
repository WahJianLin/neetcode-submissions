class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ret = []
        cur = []
        nl = len(nums)
        total = 0

        #check not over nums len
        def dfs(i, total):
            if i >= nl:
                return
            # exceed case
            if total > target:
                return
            # found case
            if total == target:
                ret.append(cur.copy())
                return
            # logic
            # repeat
            cur.append(nums[i])
            total += nums[i]
            dfs(i, total)
            
            # go next
            cur.pop()
            total -= nums[i]
            dfs(i + 1, total)
        dfs(0, total)
        return ret