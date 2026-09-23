class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        s = set()
        l = 0 
        for r in range(len(nums)):
            if r - l > k:
                s.remove(nums[l])
                l+=1
            rVal = nums[r]
            if rVal in s:
                return True
            s.add(rVal)

        return False