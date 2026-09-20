class Solution:
    # m rows
    # n cols
    def uniquePaths(self, m: int, n: int) -> int:

        arr = [([0]*n) for _ in range(m)] 
        arr[m-1][n-1]=1
        def dp(r,c):
            if r == m or c == n:
                return 0
            count = 0
            val = arr[r][c]
            if val != 0:
                return val
            count += dp(r+1,c)
            count += dp(r,c+1)
            arr[r][c]=count
            return count
        dp(0,0)
        return arr[0][0]