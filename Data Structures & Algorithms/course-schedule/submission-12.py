class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        m = {}
        seen = set()
        for c, p in prerequisites:
            val = m.get(c,[])
            val.append(p)
            m[c] = val
        def dfs(cur):
            if cur not in m:
                return True
            if cur in seen:
                return False
            seen.add(cur)
            req = m[cur]
            for r in req:
                if dfs(r) == False:
                    return False
            seen.remove(cur)
            m[cur] = [] 
            return True
            
                
        for c, p in prerequisites:
            seen=set()
            if dfs(c) == False:
                return False
        return True