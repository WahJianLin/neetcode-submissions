class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        max_count = 0

        for num in nums:
            if num-1 not in nums:
                count = 0
                i = num
                while i in numSet:
                    count+=1
                    i+=1
                max_count = max(count, max_count)
             
        return max_count