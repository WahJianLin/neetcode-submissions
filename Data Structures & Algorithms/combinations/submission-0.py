class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ret = []
        cur = []
        def dfs(i):
            if len(cur) == k:
                ret.append(cur.copy())
                return
            if i > n:
                return
            for j in range(i,n+1):

                cur.append(j)
                dfs(j+1)
                cur.pop()
        dfs(1)
        return ret