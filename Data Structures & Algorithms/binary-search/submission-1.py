class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bs(l,r,arr,t):
            if r < l:
                return -1
            m = l + (r - l) // 2
            mVal = arr[m]
            if t < mVal:
                right = m - 1
                return bs(l,right,arr,t)
            elif mVal < t:
                left = m + 1
                return bs(left,r,arr,t)
            else:
                return m
        return bs(0,len(nums)-1,nums,target)
