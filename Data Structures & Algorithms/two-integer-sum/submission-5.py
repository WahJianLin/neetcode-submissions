class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        for i in range(len(nums)):
            numMap[nums[i]] = i

        for i in range(len(nums)):
            val = nums[i]
            diff = target - val
            if diff in numMap:
                j = numMap[diff]
                if i != j:
                    return [i, j]
        return []
            