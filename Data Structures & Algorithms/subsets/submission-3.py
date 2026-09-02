class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []
        arr = []
        numLen = len(nums)
        def dfs(pos):
            if pos >= numLen:
                ret.append(arr.copy())
                return
            arr.append(nums[pos])
            dfs(pos+1)
            arr.pop()
            dfs(pos+1)
        dfs(0)
        return ret