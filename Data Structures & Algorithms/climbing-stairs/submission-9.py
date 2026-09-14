class Solution:
    def climbStairs(self, n: int) -> int:
        pre = 0
        cur = 1
        for i in range(n):
            tPre = pre
            tCur = cur
            pre = cur
            cur = tPre +tCur
        return cur