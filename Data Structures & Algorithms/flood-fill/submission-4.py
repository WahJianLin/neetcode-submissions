class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rl = len(image)
        cl = len(image[0])

        seen = set()

        d = deque()
        d.append((sr,sc))

        orig = image[sr][sc]
        while d:
            r,c = d.popleft()
            if r < 0 or c < 0 or r == rl or c == cl or (r,c) in seen or image[r][c] != orig:
                continue
            seen.add((r,c))
            image[r][c] = color
            d.append((r+1,c))
            d.append((r-1,c))
            d.append((r,c+1))
            d.append((r,c-1))

        return image