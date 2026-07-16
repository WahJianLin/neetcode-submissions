class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        high = -1
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                high = max(high, arr[j])
            arr[i] = high
            high = -1

        return arr