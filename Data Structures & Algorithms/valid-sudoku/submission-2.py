class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        boxes = {}
        for r in range(len(board)):
            for c in range(len(board[0])):
                val = board[r][c]
                if val != ".":
                    sel_r = rows.setdefault(r, set())
                    sel_c = cols.setdefault(c, set())
                    sel_b = boxes.setdefault((r//3,c//3), set())
                    if val in sel_r or val in sel_c or val in sel_b:
                        return False
                    sel_r.add(val)
                    sel_c.add(val)
                    sel_b.add(val)
        return True
