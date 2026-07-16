class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        arrLen = len(nums)
        ret = [0] * arrLen*2
        for i in range(arrLen):
            val = nums[i]
            ret[i] = val
            ret[i+arrLen] = val 
        return ret
        