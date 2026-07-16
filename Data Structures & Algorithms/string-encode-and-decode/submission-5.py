class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""
        for i in strs:
            print(1)
            ret += "(:-:)"
            ret += i
        return ret

    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
        ret = s[5:].split("(:-:)")
        return ret

