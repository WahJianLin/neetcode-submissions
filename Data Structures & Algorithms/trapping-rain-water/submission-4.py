class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0 
        r = len(height) - 1
        lm = height[l]
        rm = height[r]
        rain = 0

        while l<r:
            lVal = height[l]
            rVal = height[r]
            if lVal < rVal:
                l+=1
                newLH= height[l]
                lDiff = lm - newLH
                if lDiff > 0:
                    rain += lDiff
                lm = max(lm, newLH)
            else:
                r-=1
                newRH= height[r]
                rDiff = rm - newRH
                if rDiff > 0:
                    rain += rDiff
                rm = max(rm, newRH)

        return rain