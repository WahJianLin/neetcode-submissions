class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap = {}
        tMap = {}
        for i in range(len(s)):
            sMap[s[i]] = sMap.get(s[i], 0) + 1
        
        for i in range(len(t)):
            tMap[t[i]] = tMap.get(t[i], 0) + 1
        print(sMap, tMap)
        return sMap == tMap