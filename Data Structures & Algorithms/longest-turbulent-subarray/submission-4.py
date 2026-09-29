class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 1
        ret = 1

        prevRising = None

        count = 1
        for r in range(1,len(arr)):
            cur = arr[r]
            pre = arr[r-1]
            if pre < cur and prevRising != True:
                prevRising = True
                count+=1
            elif pre > cur and prevRising != False:
                prevRising = False
                count+=1
            elif pre == cur:
                prevRising = None
                count = 1
            else:
                prevRising = (pre < cur)
                count = 2
            ret = max(count,ret)
        return ret
