class Solution:
    def rob(self, nums: List[int]) -> int:
        ml = len(nums)
        if ml == 1:
            return nums[0]
        away1,away2,away3 = 0,0,0
        for i in range(1,ml):
            temp = max(away3,away2) + nums[i]
            away3 = away2
            away2 = away1
            away1 = temp
        skipedFirstMax = max(away2, away1)
        away1,away2,away3 = 0,0,0
        for i in range(0,ml-1):
            temp = max(away3,away2) + nums[i]
            away3 = away2
            away2 = away1
            away1 = temp
        return max(skipedFirstMax,away1,away2)