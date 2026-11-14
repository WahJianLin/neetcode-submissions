class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        ROWS = len(nums)
        if sum(nums) % 2 == 1:
            return False
        COLS = sum(nums)//2 
        half = COLS
        arr = [[False] * (COLS + 1) for _ in range(ROWS)]
        for r in range(ROWS):
            arr[r][0] = True
        for c in range(1, COLS+1):
            arr[0][c] = c - nums[0] == 0
            
        for r in range(1,ROWS):
            for c in range(1, COLS+1):
                og = arr[r-1][c]
                diff = c - nums[r]
                if diff > -1:
                    og = og or arr[r-1][diff]
                arr[r][c] = og
                
        return arr[ROWS-1][COLS]