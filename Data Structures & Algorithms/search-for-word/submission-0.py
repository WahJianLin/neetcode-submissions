class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        wl = len(word)
        ROWS = len(board)
        COLS = len(board[0])
        seen = set()
        neighbors = [[1,0],[-1,0],[0,1],[0,-1]]
        def dfs(i, r, c):
            if r < 0 or c < 0 or r == ROWS or c == COLS or ((r,c)) in seen or board[r][c] != word[i]:
                return False
            if i == wl -1:
                return True
            seen.add((r,c))
            for nr, nc in neighbors:
                rr = r + nr
                cc = c + nc
                if dfs(i + 1, rr,cc):
                    return True
            seen.remove((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(0,r,c):
                    return True
        return False