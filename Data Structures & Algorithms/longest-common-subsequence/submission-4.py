class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        ROWS = len(text1)
        COLS = len(text2)

        arr = [([0]* (COLS+1)) for i in range(ROWS+1)]

        def dp(r,c):
            if r == ROWS or c == COLS:
                return 0
            if arr[r][c] != 0:
                return arr[r][c]
            print(text1[r],text2[c])
            if text1[r] == text2[c]:
                print('found')
                arr[r][c] = dp(r+1,c+1)+1
            else:
                arr[r][c] = max(dp(r+1,c), dp(r,c+1))
            
            return arr[r][c]
        dp(0,0)
        return arr[0][0]