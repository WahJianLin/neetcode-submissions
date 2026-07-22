class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {1:1, 2:2}
        def recur(n: int, memo):
            if n in memo:
                return memo[n]
            val = recur(n-1, memo) + recur(n-2, memo)
            memo[n] = val
            return val
        
        return recur(n,memo)