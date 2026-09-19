class Solution:
    def rob(self, nums: List[int]) -> int:
        h1 = 0
        h2 = 0
        h3 = 0
        
        for i in range(len(nums)):
            if i<2:
                h1=h2
                h2=h3
                h3 = nums[i]
            else:
                temp = max(h1,h2)
                h1=h2
                h2=h3
                h3 = temp + nums[i]

        return max(h2,h3)