class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = set()
        cols = {}
        boxes = {}
        length = len(board)
        for r in range(length):
            for c in range(length):
                val = board[r][c]
                if val != '.':
                    cSet = cols.get(c, set())
                    bSet = boxes.get((r//3,c//3),set())
                    if val in rows or val in cSet or val in bSet:
                        return False
                    rows.add(val)
                    
                    cSet.add(val)
                    cols[c] = cSet

                    bSet.add(val)
                    boxes[(r//3,c//3)] = bSet
            rows = set()
        print(boxes)
        return True
