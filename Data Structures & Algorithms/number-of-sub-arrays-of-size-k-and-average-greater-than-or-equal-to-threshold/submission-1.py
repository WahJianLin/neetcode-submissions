class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        total = 0
        count = 0
        l = 0
        for r in range(len(arr)):
            total += arr[r]
            if r - l +1 >= k:
                avgVal = total / k
                if avgVal >= threshold:
                    count+=1
                
                total -= arr[l]
                l += 1

        return count
        
