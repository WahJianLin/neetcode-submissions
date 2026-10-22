class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        ld = len(digits)
        lettersMap = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }
        ret = []
        cur = []

        def dfs(i):
            if len(cur) == ld:
                ret.append("".join(cur))
            if i+1 > ld:
                return
            print(i,ld,int(digits[i]))
            letters = lettersMap[int(digits[i])]
            for l in letters:
                cur.append(l)
                dfs(i+1)
                cur.pop()
        dfs(0)

        print(ret)
        return ret