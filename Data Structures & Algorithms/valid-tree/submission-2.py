class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n == 1:
            return True
        m = {}
        for s,l in edges:
            sm = m.get(s,[])
            lm = m.get(l,[])
            if l not in sm:
                sm.append(l)
            m[s] = sm

            if s not in lm:
                lm.append(s)
            m[l] = lm
            
        seen = set()
        traversed = set()
        last = None

        def dfs(cur, last):
            print(cur)
            if cur in seen or cur not in m: #there is a cycle
                return False
            seen.add(cur)
            traversed.add(cur)
            ne = m[cur]
            for x in ne:
                if x == last:
                    continue

                if not dfs(x, cur):
                    return False
            seen.remove(cur)
            return True

        if not dfs(0, None): #checks for cycle
            return False
        if len(traversed) != n: #checks if the tree is connected
            return False
        return True