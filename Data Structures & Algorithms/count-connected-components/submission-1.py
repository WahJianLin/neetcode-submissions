class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        ret = 0
        m = {}
        seen = set()
        traversed = set()
        for a,b in edges:
            am = m.get(a,[])
            am.append(b)
            m[a] = am

            bm = m.get(b,[])
            bm.append(a)
            m[b] = bm
        def dfs(cur):
            if cur in seen or cur not in m:
                return
            req = m[cur]
            traversed.add(cur)
            seen.add(cur)
            for r in req:
                dfs(r)
            m.pop(cur)

        for i in range(n):
            if i not in traversed:
                dfs(i)
                ret += 1
        return ret