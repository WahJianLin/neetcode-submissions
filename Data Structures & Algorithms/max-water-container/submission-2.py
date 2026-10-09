class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxV = 0
        while l < r:
            dist = r-l
            lh = heights[l]
            rh = heights[r]
            sides = min(lh,rh)
            maxV = max(maxV, (sides*dist))
            if lh < rh:
                l+=1
            else:
                r-=1
        return maxV