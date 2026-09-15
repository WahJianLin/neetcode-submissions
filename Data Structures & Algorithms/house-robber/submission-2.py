class Solution:
    def rob(self, nums: List[int]) -> int:
        
        away1, away2, away3 = 0,0,0

        for i in range(len(nums)):
            temp = max(away3,away2) + nums[i]
            away3=away2
            away2 =away1
            away1=temp
        return max(away1,away2)