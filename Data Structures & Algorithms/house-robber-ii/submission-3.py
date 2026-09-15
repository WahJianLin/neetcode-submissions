class Solution:
    def rob(self, nums: List[int]) -> int:
        ml = len(nums)
        if ml == 1:
            return nums[0]
        saved = ml*[0]
        for i in range(1, ml):
            val = 0
            if i < 2:
                val = nums[i]
            else:
                val = max(saved[i-3],saved[i-2]) + nums[i]
            saved[i] = max(val, saved[i])
        for i in range(0, ml-1):
            val = 0
            if i < 2:
                val = nums[i]
            elif i == 2:
                val = nums[i] + saved[i-2]
            else:
                val = max(saved[i-3],saved[i-2]) + nums[i]
            saved[i] = max(val, saved[i])
        return max(saved[ml-3], saved[ml-2], saved[ml-1])