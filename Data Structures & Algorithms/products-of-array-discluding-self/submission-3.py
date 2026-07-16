class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = []
        ret = []
        val = 1
        numLen = len(nums)
        for i in range(numLen):
            val *= nums[i]
            prefix.append(val)
        val = 1
        for i in range(numLen-1,-1,-1):
            val *= nums[i]
            suffix.insert(0,val)
        for i in range(numLen):
            val = 1
            if i > 0:
                val *= prefix[i-1]
            if i < numLen - 1:
                val *= suffix[i+1]
            ret.append(val)
        
        return ret