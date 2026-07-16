class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_count = 0

        for val in nums:
            if val-1 not in num_set:
                pos = val
                count = 0
                while pos in num_set:
                    count += 1
                    pos += 1
                max_count = max(count, max_count)

        return max_count