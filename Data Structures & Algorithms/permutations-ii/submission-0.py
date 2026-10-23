class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ret = []
        nl = len(nums)

        def dfs(i):
            if i == nl-1:
                return [[nums[i]]]

            temp = []
            perm = dfs(i+1)
            val = nums[i]
            for p in perm:
                for j in range(len(p) + 1):
                    copy = p.copy()
                    copy.insert(j,val)
                    if copy not in temp:
                        temp.append(copy)
            return temp
        return dfs(0)