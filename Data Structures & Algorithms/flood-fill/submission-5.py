class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS = len(image)
        COLS = len(image[0])
        seen = set()
        t = image[sr][sc]
        neighbors = [[1,0],[-1,0],[0,1],[0,-1]]

        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r,c) in seen or image[r][c] != t:
                return
            val = image[r][c]
            seen.add((r,c))
            if val == t:
                image[r][c] = color
            for nr, nc in neighbors:
                rr = r + nr
                cc = c + nc
                dfs(rr,cc)
            return


        dfs(sr, sc)

        return image
