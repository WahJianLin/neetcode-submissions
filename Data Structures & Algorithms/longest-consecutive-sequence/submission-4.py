class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        print(num_set)
        max_count = 0

        for val in nums:
            count = 1
            pos = val - 1
            while pos in num_set:
                count+=1
                pos -= 1
            max_count = max(count, max_count)

        return max_count