class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        init = amount + 1
        lc = len(coins)
        memo = {}
        def dfs(i, a):
            if a == 0:
                return 0
            if i == lc:
                return init
            if (i,a) in memo:
                return memo[(i,a)]

            # skip
            count = min(init, dfs(i+1,a))

            aDiff=a - coins[i]
            if aDiff >=0:
                count = min(count, dfs(i,aDiff) +1)
            memo[(i,a)] = count
            return count

        ret = dfs(0,amount)
        return -1 if ret == init else ret
