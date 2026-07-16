class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for i in nums:
            val = count.get(i, 0) + 1
            count[i] = val
        
        countList = []
        for i in count:
            countList.append([i, count[i]])

        countList.sort(key=lambda x: x[1])
        res = []

        for e in range(k):
            val = countList.pop()
            res.append(val[0])

        return res