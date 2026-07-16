class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        for i in range(len(nums)):
            val = nums[i]
            diff = target - nums[i]
            if diff in numMap:
                return [numMap[diff], i]
            numMap[val] = i

                