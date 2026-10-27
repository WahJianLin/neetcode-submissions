class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ret = []
        adj = {}
        visit = set()
        path = set()
        for n in range(numCourses):
            adj[n] = []
        for c, p in prerequisites:
            adj[c].append(p)

        def dfs(i):
            if i in path:
                return False
            if i in visit:
                return True
            path.add(i)
            visit.add(i)
            for j in adj[i]:
                if not dfs(j):
                    return False
            path.remove(i)
            ret.append(i)
            return True

        for n in range(numCourses):
            if not dfs(n):
                return False
        return True