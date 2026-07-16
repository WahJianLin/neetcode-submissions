class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ret = []
        cur = []
        size = len(nums)
        def dfs(i):
            t = sum(cur)
            if t == target:
                print('found', cur, t)
                ret.append(cur.copy())
                return

            if i >= size or t > target:
                print('no', cur, t)
                return

            val = nums[i]
            cur.append(val)
            dfs(i)
            cur.pop()
            dfs(i+1)

        dfs(0)
        return ret