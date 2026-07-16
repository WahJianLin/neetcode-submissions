class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap = {}
        tMap = {}
        for i in s:
            val = sMap.get(i, 0) + 1
            sMap[i] = val
        for i in t:
            val = tMap.get(i, 0) + 1
            tMap[i] = val
        return sMap == tMap