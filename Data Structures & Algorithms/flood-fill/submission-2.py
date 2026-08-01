class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rl = len(image)
        cl = len(image[0])
        orig = image[sr][sc]
        seen = set()
        def dfs(r,c):
            #failed base case
            if r < 0 or c < 0 or r == rl or c == cl or (r,c) in seen or image[r][c] != orig:
                return
            image[r][c] = color
            seen.add((r,c))
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
            

        dfs(sr,sc)
        return image