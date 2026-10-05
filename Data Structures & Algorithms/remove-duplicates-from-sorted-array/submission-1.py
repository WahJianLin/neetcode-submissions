class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nl = len(nums)
        if not nums:
            return -1
        l = 0
        for r in range(1,nl):
            if nums[l] != nums[r]:
                l+=1
                nums[l] = nums[r]
        return l + 1