class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==0:
            return 0
        lowest = prices[0]
        profit = 0
        for i in prices:
            if i < lowest:
                lowest = i
            else:
                diff = i-lowest
                profit = max(profit, diff)

        return profit
