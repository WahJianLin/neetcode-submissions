class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ret = [[]]

        for n in nums:
            temp = []
            for p in ret:
                for j in range(len(p)+1):
                    copy = p.copy()
                    copy.insert(j, n)
                    if copy not in temp:
                        temp.append(copy)
            
            ret = temp

        return ret