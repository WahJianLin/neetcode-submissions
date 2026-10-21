class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []
        cur = []
        nl = len(nums)
        
        def dfs(i, cur, ret):
            if i >= nl:
                ret.append(cur.copy())
                return

            
            val = nums[i]
            cur.append(val)
            dfs(i+1, cur, ret)
            cur.pop()
            dfs(i+1, cur, ret)
                
        dfs(0, cur, ret)
        return ret