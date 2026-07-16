class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        contains = set()
        for i in nums:
            if i in contains:
                return i
            contains.add(i)