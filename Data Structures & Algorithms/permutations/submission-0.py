class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = []
        nl = len(nums)
        def dfs(i):
            if i == nl-1:
                return [[nums[i]]]
            cur = []
            prev = dfs(i+1)
            for p in prev:
                for j in range(len(p)+1):
                    copy = p.copy()
                    copy.insert(j,nums[i])
                    cur.append(copy)
            return cur
        
        return dfs(0)