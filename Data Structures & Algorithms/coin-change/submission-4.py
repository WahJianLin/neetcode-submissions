class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = [amount+1] * (amount+1)
        cache[0]=0

        for a in range(1,amount+1):
            for c in coins:
                val = a - c
                if val>=0:
                    cache[a] = min(1+cache[val],cache[a])
        print(cache)
        return -1 if cache[amount] == amount+1 else cache[amount]