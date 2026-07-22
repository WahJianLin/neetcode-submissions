class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        total = m+n
        spot = 0
        for i in range(m, total):
            if spot < n:
                nums1[i] = nums2[spot]
                spot+=1
        nums1.sort()
        