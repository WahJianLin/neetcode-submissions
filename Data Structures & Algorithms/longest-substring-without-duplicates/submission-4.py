class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cont = set()
        l = 0
        ret = 0
        for r in range(len(s)):
            val = s[r]
            while val in cont:
                tar = s[l]
                l+=1
                cont.remove(tar)
            cont.add(val)
            ret = max(ret, len(cont))
                


        return ret