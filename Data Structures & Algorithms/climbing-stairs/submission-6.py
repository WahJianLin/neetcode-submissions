class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {0:0, 1:1, 2:2}
        def rec(n, cache):
            if n in cache:
                return cache[n]
            val = rec(n-1, cache) + rec(n-2, cache)
            cache[n] = val
            return val
        print(cache[1])
        return rec(n, cache)