class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ret = 0
        rep = set()
        l = 0
        for r in range(len(s)):
            rLet = s[r]
            while rLet in rep:
                rep.remove(s[l])
                l+=1
            rep.add(rLet)
            ret = max(ret, r-l+1)
        return ret