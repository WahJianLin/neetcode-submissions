class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        high = -1
        for i in range(len(arr)-1,-1,-1):
            temp = arr[i]
            arr[i] = high
            high = max(high,temp)
        return arr