class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        lt1 = len(text1)
        lt2 = len(text2)
        arr = [((lt2+1) * [0]) for _ in range(lt1+1)]
        
        for l1 in range(lt1-1,-1,-1):
            for l2 in range(lt2-1,-1,-1):
                if text1[l1]==text2[l2]:
                    arr[l1][l2]=arr[l1+1][l2+1]+1
                else:
                    arr[l1][l2] = max(arr[l1+1][l2],arr[l1][l2+1])
        print(arr)
        return arr[0][0]
        

  