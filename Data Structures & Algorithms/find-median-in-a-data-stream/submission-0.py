class MedianFinder:

    def __init__(self):
        self.left = [] # stores the numbers to the smaller of the median (max heap)
        self.right = [] # stores the numbers to the higher of the median (min heap)

    def addNum(self, num: int) -> None:
        # always add to right. 
        heapq.heappush(self.right,num)
        # Make sure the lowest value in the right half is not smaller than the largest value in the left half
        rVal = self.right[0]
        lVal = (self.left[0] if self.left else rVal) * -1 # we have to store in negative versions because heapq does not have a max heap version
        if rVal < lVal:
            temp = heapq.heappop(self.right) * -1
            heapq.heappush(self.left, temp)
        # we have to keep the len diff between right and left  at most 1
        rL = len(self.right)
        lL = len(self.left)
        diff = rL - lL
        if diff > 1: # too many in the right half
            temp = heapq.heappop(self.right) * -1
            heapq.heappush(self.left, temp)
        if diff < -1: # too many in the left half
            temp = heapq.heappop(self.left) * -1
            heapq.heappush(self.right, temp)
            
    def findMedian(self) -> float:
        rL = len(self.right)
        lL = len(self.left)
        if lL == 0 or rL > lL:
            return self.right[0]
        if lL > rL:
            return self.left[0] * -1
        

        return (self.right[0] + (self.left[0] * -1)) / 2
        