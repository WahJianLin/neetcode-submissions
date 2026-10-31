class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = {}
        req = {}
        for n in range(numCourses):
            adj[n] = []
            req[n] = set()
        
        for p,c in prerequisites:
            adj[c].append(p)
        
        tSort = []
        visit = set()

        def dfs(i):
            if i in visit:
                return i
            visit.add(i)

            for j in adj[i]:
                val = dfs(j)
                req[i].add(val)
                req[i].update(req[val])
                print(req[i])
            tSort.append(i)
            return(i)
        
        for n in range(numCourses):
            if len(adj[n]) > 0:
                dfs(n)
        ret = []
        print(req)
        for p,c in queries:
            ret.append(p in req[c])

        return ret