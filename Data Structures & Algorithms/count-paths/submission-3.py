class Solution:
#m = rows, n = cols
    def uniquePaths(self, m: int, n: int) -> int:
        bot = n*[0]

        for i in range(m):
            top = n*[0]
            top[n-1] = 1
            for j in range(n-2,-1,-1):
                top[j]=bot[j]+top[j+1]
                
            bot = top
        return bot[0]