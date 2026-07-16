class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ret = []
        size = len(nums)
        def dfs(i, cur, t):
            if t == target:
                ret.append(cur.copy())
                return

            if i >= size or t > target:
                return

            val = nums[i]
            t+=val
            cur.append(val)
            dfs(i,cur,t)
            cur.pop()
            t-=val
            dfs(i+1,cur,t)

        dfs(0,[],0)
        return ret