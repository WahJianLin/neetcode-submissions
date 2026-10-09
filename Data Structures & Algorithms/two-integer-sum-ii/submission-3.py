class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while r > l:
            lVal = numbers[l]
            rVal = numbers[r]
            res = lVal + rVal
            if res < target:
                l+=1
            elif res > target:
                r-=1
            else:
                return [l+1, r+1]

        return []