class Solution:
#m = rows, n = cols
    def uniquePaths(self, m: int, n: int) -> int:
        arr = [[0 for _ in range(n)] for _ in range(m)]
        
        def dp(r,c):
            if r == m or c == n:
                return 0
            if r == m-1 and c == n - 1:
                arr[r][c] = 1
                return 1
            val = arr[r][c]
            if val > 0:
                return val

            if r < m - 1:
                val += dp(r+1,c)
            
            if c < n - 1:
                val += dp(r,c+1)
            arr[r][c] = val
            return val
        
        return dp(0,0)