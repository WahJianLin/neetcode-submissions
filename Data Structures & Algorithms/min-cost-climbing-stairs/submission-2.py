class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        step1 = cost[0]
        step2 = cost[1]

        for i in range(2,len(cost)):
            temp = min(step1,step2)+cost[i]
            step1 = step2
            step2 = temp
        return min(step1,step2)