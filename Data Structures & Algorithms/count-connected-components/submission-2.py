class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = {}
        rank = {}
        up = set()

        for i in range(n):
            par[i] = i
            rank[i] = 0
            up.add(i)

        def find(e):
            p = par[e]
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p
        
        def union(e1,e2):
            p1 = find(e1)
            p2 = find(e2)

            if p1 == p2:
                return
            r1 = rank[p1]
            r2 = rank[p2]

            if r1<r2:
                par[p1] = p2
                up.remove(p1)
            elif r1>r2:
                par[p2] = p1
                up.remove(p2)
            else:
                par[p2] = p1
                rank[p1] += 1
                up.remove(p2)

        for e1,e2 in edges:
            union(e1,e2)
        return len(up)