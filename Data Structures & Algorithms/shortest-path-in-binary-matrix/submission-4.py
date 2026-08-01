class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rl = len(grid)
        cl = len(grid[0])
        if grid[0][0] == 1:
            return -1
        d = deque()
        d.append((0, 0))
        seen = set()
        adj = [[1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1]]

        path = 0

        while d:
            path += 1
            for i in range(len(d)):
                r, c = d.popleft()
                seen.add((r, c))
                if r == rl-1 and c == cl - 1:
                    return path
                for rr, cc in adj:
                    br = r + rr
                    bc = c + cc
                    if (
                        br < 0
                        or bc < 0
                        or br == rl
                        or bc == cl
                        or (br, bc) in seen
                        or grid[br][bc] == 1
                    ):
                        continue

                    d.append((br, bc))

        return -1
