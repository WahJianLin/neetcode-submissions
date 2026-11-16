class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        sl = len(strs)
        mArr = []
        nArr = []
        memo = {}

        for arr in strs:
            zeros = 0
            ones = 0
            for c  in arr:
                if c == '0':
                    zeros += 1
                if c == '1':
                    ones += 1
            mArr.append(zeros)
            nArr.append(ones)

        def dfs(i, mc, nc):
            if i == sl or mc < 0 or nc<0:
                return 0
            if (i,mc,nc) in memo:
                return memo[(i,mc,nc)]
            
            num = dfs(i+1, mc, nc)
            num2 = 0 
            if mc - mArr[i] >=0 and nc - nArr[i] >= 0:
                num2 = 1+dfs(i+1, mc - mArr[i], nc - nArr[i])
            memo[(i,mc,nc)] = max(num,num2)
            return  memo[(i,mc,nc)]

        return dfs(0, m, n)