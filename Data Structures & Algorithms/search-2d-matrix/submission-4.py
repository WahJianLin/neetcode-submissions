class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        w = len(matrix[0])-1
        for y in matrix:
            if target <= y[w]:
                l = 0
                r = w
                while l<=r:
                    m = (l+r) // 2
                    val = y[m]
                    if val == target:
                        return True
                    if val < target:
                        l = m + 1
                    if target < val:
                        r = m - 1
                return False

        return False