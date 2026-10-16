class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        par = {}
        rank = {}
        owner = {}
        
        for a in range(len(accounts)):
            for i in range(1,len(accounts[a])):
                email = accounts[a][i]
                owner[email] = a
                par[email] = email
                rank[email] = 0

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
            elif r1>r2:
                par[p2] = p1
            else:
                par[p2] = p1
                rank[p1]+=1

        for a in accounts:
            name = a[0]
            mEmail = a[1]
            for i in range(2,len(a)):
                email = a[i]
                union(mEmail, email)

        formatAcc = {}
        for k,v in par.items():
            root = find(v)
            emailId = owner[root]
            acc = formatAcc.get(emailId, [accounts[emailId][0]])
            acc.append(k)
            formatAcc[emailId] = acc
        
        return list(formatAcc.values())



