class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return False
        sortNums = sorted(nums)
        for i in range(1,len(nums)):
            if sortNums[i] == sortNums[i-1]:
                return True
            
        return False