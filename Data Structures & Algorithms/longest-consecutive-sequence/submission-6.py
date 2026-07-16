class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq = {}
        max_count = 0
        for num in nums:
            val = seq.get(num-1,0) + 1
            seq[num] = val
            i = num + 1
            while i in seq:
                val += 1
                seq[i] = val
                i += 1
            max_count = max(val, max_count)
             
        return max_count