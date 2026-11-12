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

        def dfs(i, mc, nc, memo):
            key = (i,mc,nc)
            if mc < 0 or nc < 0:
                return -1
            if key in memo:
                return memo[key]
            if  mc < 0 or nc < 0:
                return 0
            if i == sl:
                return 0
            mcDiff = mc - zeroArr[i]
            ncDiff = nc - oneArr[i]
            memo[key] = max(1+dfs(i+1, mcDiff, ncDiff, memo), dfs(i+1, mc, nc, memo))
            return memo[key]
            
        return dfs(0,m,n, memo)