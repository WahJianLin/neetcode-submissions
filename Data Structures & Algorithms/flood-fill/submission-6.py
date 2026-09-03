class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS = len(image)
        COLS = len(image[0])
        seen = set()
        t = image[sr][sc]
        neighbors = [[1,0],[-1,0],[0,1],[0,-1]]
        d = deque()
        d.append((sr,sc))

        while d:
            for i in range(len(d)):
                r,c = d.popleft()
                if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r,c) in seen or image[r][c] != t:
                    continue
                image[r][c] = color
                seen.add((r,c))
                for nr,nc in neighbors:
                    rr = r + nr
                    cc = c + nc
                    d.append((rr,cc))
        return image
