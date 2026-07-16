class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {1:1, 2:2}
        def rec(s, m):
            if s in m:
                return m[s]
            val1 = rec(s-1, m)
            val2 = rec(s-2, m)
            m[s-1] = val1
            m[s-2] = val2
            return val1 + val2
        return rec(n, memo)