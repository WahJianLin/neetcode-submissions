class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ret = []
        arr = []
        numsLen = len(nums)
        def dfs(pos):
            if pos >= numsLen:
                sortedArr = sorted(arr.copy())
                if sortedArr not in ret:
                    ret.append(sortedArr)
                return
            arr.append(nums[pos])
            dfs(pos+1)
            arr.pop()
            dfs(pos+1)
        dfs(0)

        return ret