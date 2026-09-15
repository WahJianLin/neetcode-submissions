class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cl = len(cost)
        away2 = 0
        away1 = 0
        for i in range(cl):
            temp = min(away2,away1) + cost[i]
            away2 = away1
            away1= temp
        return min(away2, away1)