class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [amount+1] * (amount + 1)
        memo[0] = 0
        for a in range(1,amount+1):
            for c in coins:
                rem = a - c
                if rem >= 0:
                    memo[a] = min(memo[a], 1 + memo[rem])
                
        print(memo)
        return -1 if memo[amount] == amount+1 else memo[amount]