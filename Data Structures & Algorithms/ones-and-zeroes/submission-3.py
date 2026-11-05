class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        sl = len(strs)
        zeroArr = []
        oneArr = []
        memo = {}

        for arr in strs:
            zeros = 0
            ones = 0
            for c  in arr:
                if c == '0':
                    zeros += 1
                if c == '1':
                    ones += 1
            zeroArr.append(zeros)
            oneArr.append(ones)

        def dfs(i, zeroC, oneC):
            if i == sl:
                return 0
            if (i, zeroC, oneC) in memo:
                return memo[(i, zeroC, oneC)]
            ret = dfs(i+1, zeroC, oneC)
            ones = oneArr[i]
            zeros = zeroArr[i]
            if oneC >= ones and zeroC >= zeros:
                newOnes = oneC - ones
                newZeros = zeroC - zeros
                ret = max(dfs(i+1, newZeros, newOnes) +1,ret)
            memo[(i, zeroC, oneC)] = ret
            return ret
            
        return dfs(0,m,n)