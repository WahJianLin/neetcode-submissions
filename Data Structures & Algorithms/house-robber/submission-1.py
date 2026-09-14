class Solution:
    def rob(self, nums: List[int]) -> int:
        ret = 0

        saved = len(nums)*[0]
        ml = len(nums)

        
        for i in range(len(nums)):
            if i < 2:
                saved[i] = nums[i]
            elif i == 2:
                saved[i] = saved[i-2] + nums[i]
            else:
                val1 = saved[i-2]
                val2 = saved[i-3]
                if val1>val2:
                    saved[i] = val1+nums[i]
                else:
                    saved[i] = val2+nums[i]

        return saved[ml-1] if saved[ml-1] > saved[ml-2] else saved[ml-2]