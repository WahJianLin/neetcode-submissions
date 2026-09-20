class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        cache[0]=0

        for a in range(1,amount+1):
            for c in coins:
                val = a - c
                if val>=0:
                    print('hi')
                    cache[a] = min(1+cache.get(val,amount+1), cache.get(a,amount+1))

        print(cache)
        return -1 if amount not in cache or cache[amount] == amount+1 else cache[amount]