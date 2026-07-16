class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0 
        r = len(heights) - 1
        ret=0
        while l<r:
            lh = heights[l]
            rh = heights[r]
            m = min(lh, rh)
            dist = r-l
            ret = max(ret, m * dist)
            if lh<rh:
                l+=1
            else:
                r-=1
        return ret
        