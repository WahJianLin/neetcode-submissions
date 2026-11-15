class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        ROWS = len(coins)
        COLS = amount + 1
        arr = [[amount+1] * COLS for i in range(ROWS)]
        for r in range(0,ROWS):
            arr[r][0] = 0
        for amount in range(1,COLS):
            if amount % coins[0] == 0:
                arr[0][amount] = amount // coins[0]
        for r in range(1,ROWS):
            for amount in range(1,COLS):
                num = arr[r-1][amount]
                diff = amount - coins[r]
                if diff >= 0:
                    num = min(num, arr[r][diff]+1)
                arr[r][amount] = num
        ret = arr[ROWS-1][COLS-1]
        return -1 if ret > amount else ret