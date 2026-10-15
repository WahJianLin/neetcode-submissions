class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = {}
        rank = {}

        for i in range(1,len(edges)+1):
            par[i] = i
            rank[i] = 0

        def find(e): # finds highest ancestor / parent
            p = par[e]
            while p != par[p]:
                par[p] = par[par[p]] #sets parent to grand parent
                p = par[p]
            return p

        def union(e1, e2):
            p1 = find(e1)
            p2 = find(e2)

            if p1 == p2:
                print(p1,p2)
                return False 

            r1 = rank[p1]
            r2 = rank[p2]

            if r1 < r2:
                par[p1] = p2
            elif r1 > r2:
                par[p2] = p1
            else:
                par[p2] = p1
                rank[p1] += 1
            return True

        for e1,e2 in edges:
            if not union(e1, e2):
                return [e1,e2]
        return []


