class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {}
        for n in range(numCourses):
            adj[n] = []
        for c, p in prerequisites:
            adj[c].append(p)

        ret = []
        visit = set()
        path = set()

        def dfs(i):
            if i in path:
                return False
            if i in visit:
                return True
            visit.add(i)
            path.add(i)

            for j in adj[i]:
                if not dfs(j):
                    return False
            path.remove(i)
            ret.append(i)
            return True
        
        for n in range(numCourses):
            if not dfs(n):
                return []

        return ret