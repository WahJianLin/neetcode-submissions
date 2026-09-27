class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charArr = [0]*26
        l = 0
        ret = 0
        for r in range(len(s)):
            pos = ord(s[r])-65
            charArr[pos] = charArr[pos]+1
            longest = max(charArr)
            curLen = r - l +1
            while curLen - longest > k and l < len(s)+1:
                lpos = ord(s[l])-65
                charArr[lpos] = charArr[lpos] - 1
                l += 1
                curLen = r - l +1
                longest = max(charArr)
            ret = max(ret, curLen)
        return ret