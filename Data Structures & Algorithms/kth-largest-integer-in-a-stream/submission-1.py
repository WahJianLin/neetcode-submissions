class KthLargest:
    
    def __init__(self, k: int, nums: List[int]):
        print(nums)
        heapq.heapify(nums)

        while len(nums)>k:
            heapq.heappop(nums)
        print(nums)
        self.k = k
        self.nums = nums
        

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        if len(self.nums)>self.k:
            heapq.heappop(self.nums)
        return self.nums[0]
