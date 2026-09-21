class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        ROWS = len(text1)
        COLS = len(text2)
        bot = [0]* (COLS+1)

        for r in range(ROWS-1,-1,-1):
            top = [0]* (COLS+1)
            for c in range(COLS-1,-1,-1):
                if text1[r] == text2[c]:
                    top[c] = bot[c+1] +1
                else:
                    top[c] = max(bot[c],top[c+1])
            bot = top
        print(bot)
        
        return bot[0]