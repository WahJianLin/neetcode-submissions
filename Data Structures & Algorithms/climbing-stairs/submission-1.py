class Solution:
    def climbStairs(self, n: int) -> int:
        def rec(s):
            if s == 1 or s == 2:
                return s
            return rec(s-1) + rec(s-2)
        return rec(n)