class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        size = len(candidates)
        nums= sorted(candidates)
        def dfs(i, cur, t):
            if t == target:
                copy = cur.copy()
                if copy not in ret:
                    ret.append(copy)
                return
            if t > target or i >= size:
                return
            val = nums[i]
            cur.append(val)
            t+=val
            
            dfs(i+1, cur, t)
            cur.pop()
            t-=val
            dfs(i+1, cur, t)


        dfs(0, [], 0)
        return ret