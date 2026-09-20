class Solution:
    def rob(self, nums: List[int]) -> int:
        h1,h2,h3 = 0, 0 ,0 
        if len(nums)==1:
            return nums[0]
        for i in range(1,len(nums)):
            temp = max(h1,h2)
            h1=h2
            h2=h3
            h3 = temp + nums[i]
        ret = max(h2,h3)
        h1,h2,h3 = 0, 0 ,0 

        for i in range(len(nums)-1):
            temp = max(h1,h2)
            h1=h2
            h2=h3
            h3 = temp + nums[i]
        return max(h2,h3,ret)