class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 1
        ret = 0

        prevHigher = None

        count = 1
        for r in range(1,len(arr)):
            cur = arr[r]
            pre = arr[r-1]
            print(r,'=',pre,cur, count)
            if pre < cur and prevHigher != True:
                prevHigher = True
                count+=1
            elif pre > cur and prevHigher != False:
                prevHigher = False
                count+=1
            elif pre == cur:
                prevHigher = None
                count = 1
            else:
                prevHigher = (pre < cur)
                count = 2
            ret = max(count,ret)
        return ret
