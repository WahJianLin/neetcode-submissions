class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []
        cur = []
        size = len(nums)
        def dfs(i):
            if i == size:
                ret.append(cur.copy())
                return
            cur.append(nums[i])
            dfs(i+1)
            cur.pop()
            dfs(i+1)
        dfs(0)
        return ret

