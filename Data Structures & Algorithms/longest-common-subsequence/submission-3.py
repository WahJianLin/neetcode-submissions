class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        lt1 = len(text1)
        lt2 = len(text2)
        bot = (lt2+1) * [0]
  
        for l1 in range(lt1-1,-1,-1):
            top = (lt2+1) * [0]
            for l2 in range(lt2-1,-1,-1):
                if text1[l1]==text2[l2]:
                    top[l2] = bot[l2+1] + 1
                else:
                    top[l2]=max(bot[l2],top[l2+1])
            bot = top
        return bot[0]
        

  