class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            l = 0
            r = len(row) -1
            if row[0] <= target and target <= row[r]:
                while l <= r:
                    m = l + (r - l) // 2
                    mVal = row[m]
                    if mVal < target:
                        l = m + 1
                    elif target < mVal:
                        r = m - 1
                    else:
                        return True
        return False