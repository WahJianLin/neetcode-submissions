class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = re.sub("[^A-Za-z0-9]+","",s).lower()
        l=0
        r=len(filtered)-1
        while l<r:
            if filtered[l] != filtered[r]:
                return False
            l+=1
            r-=1
        return True