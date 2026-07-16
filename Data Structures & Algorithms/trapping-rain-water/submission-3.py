class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        ml = 0
        mr = 0
        count = 0
        
        while l < r:
            hl = height[l]
            hr = height[r]
            if hl<hr:
                diff = ml - hl
                if diff > 0:
                    count += diff
                ml = max(ml, hl)
                l+=1
            else:
                diff = mr - hr
                if diff > 0:
                    count += diff
                mr = max(mr, hr)
                r-=1
        return count