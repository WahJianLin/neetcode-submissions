class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        size = 0
        pointer = 0 
        for i in range(len(nums)):
            print(i)
            if nums[i] != val:
                nums[pointer] = nums[i]
                pointer +=1
                size +=1
        return size
        