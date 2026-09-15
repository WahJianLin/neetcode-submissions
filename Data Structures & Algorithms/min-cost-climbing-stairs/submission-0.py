class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cl = len(cost)
        saved = cl * [0]

        for i in range(cl):
            if i < 2:
                saved[i] = cost[i]
            else:
                saved[i] = min(saved[i-1],saved[i-2]) + cost[i]
        return min(saved[cl-1],saved[cl-2])