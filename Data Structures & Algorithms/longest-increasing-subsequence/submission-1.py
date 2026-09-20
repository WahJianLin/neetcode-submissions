class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        nl = len(nums)
        seq = nl * [0]

        for i in range(nl-1, -1, -1):
            count = 0
            iVal = nums[i]
            for j in range(i,nl):
                jVal = nums[j]
                if iVal<jVal:
                    count = max(count, seq[j])
            seq[i] = count + 1
        print(seq)
        return max(seq)