class Solution:
    # m = rows n = cols
    def uniquePaths(self, m: int, n: int) -> int:
        bot = [0]*n

        for i in range(m-1,-1,-1):
            top = [0]*n
            top[n-1]=1
            for j in range(n-2,-1,-1):
                top[j] = top[j+1] + bot[j]
            bot = top
            
        print(bot)

        return bot[0]