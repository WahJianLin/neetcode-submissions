class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l+r) // 2
            mVal = nums[m]
            if target < mVal:
                r = m - 1
            elif mVal < target:
                l = m + 1
            else:
                return m

        return -1
