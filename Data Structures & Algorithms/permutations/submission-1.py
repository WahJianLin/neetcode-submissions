class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = [[]]
        nl = len(nums)
        
        for n in nums:
            temp = []
            for p in ret:
                for i in range(len(p)+1):
                    copy = p.copy()
                    copy.insert(i,n)
                    temp.append(copy)

            ret = temp
        return ret