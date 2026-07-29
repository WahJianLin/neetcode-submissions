class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ret = []
        cur = []
        nl = len(nums)
        def dfs(i):
            if i>=nl:
                tar = cur.copy()
                tar.sort()
                if tar not in ret:
                    ret.append(tar)
                return
            cur.append(nums[i])
            dfs(i+1)
            cur.pop()
            dfs(i+1)
        dfs(0)
        return ret