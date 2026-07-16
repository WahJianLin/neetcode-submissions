class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        contains={}
        for t in strs:
            sStr = str(sorted(t))
            sList = contains.get(sStr,[])
            sList.append(t)
            contains[sStr] = sList
        return list(contains.values())
            