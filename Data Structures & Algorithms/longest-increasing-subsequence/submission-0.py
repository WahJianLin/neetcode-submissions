class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ret = 0
        nl = len(nums)
        lSeq = nl*[1]
        
        for i in range(len(nums)-1,-1, -1):
            iVal = nums[i]
            for j in range(i+1,nl):
                if iVal<nums[j]:
                    lSeq[i] = max(lSeq[j]+1,lSeq[i])

        return max(lSeq)


        # [9,1,4,2,8,3,3,9,4]
        # [1,4,3,3,2,2,2,1,1]