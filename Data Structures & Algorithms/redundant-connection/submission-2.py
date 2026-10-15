class Uf:
    def __init__(self, n) -> None:
        self.par = {}
        self.rank = {}

        for i in range(1,n+1):
            self.par[i] = i
            self.rank[i] = 0
            
    def find(self,t):
        p = self.par[t]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p
    
    def union(self, e1, e2):
        p1 = self.find(e1)
        p2 = self.find(e2)
        if p1 == p2:
            return False
        r1 = self.rank[p1]
        r2 = self.rank[p2]
        if r1 < r2:
            self.par[p1] = p2
        elif r1 > r2:
            self.par[p2] = p1
        else:
            self.par[p2] = p1
            self.rank[p1] += 1
        return True
            


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = Uf(len(edges))
        for e1, e2 in edges:
            if not uf.union(e1,e2):
                return [e1,e2]
        return []