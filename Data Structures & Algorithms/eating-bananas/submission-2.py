class Solution:
    def eatingTime(self, piles, s):
        hours = 0
        for a in piles:
            dur = math.ceil(a/s)
            hours +=dur
        return hours

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        ret = r
        while l<=r:
            speed = (l+r)//2
            et = self.eatingTime(piles,speed)
            if et <= h and et > 0 and speed < ret:
                ret = speed
            print(l,r,et)
            if et > h:
                l = speed + 1
            else:
                r = speed - 1

        return ret