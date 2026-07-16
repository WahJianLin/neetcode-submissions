class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        high = -1
        for i in range(len(arr)-1):
            high = max(arr[i+1:])
            arr[i] = high
            high = -1
        arr[len(arr)-1] = -1
        return arr