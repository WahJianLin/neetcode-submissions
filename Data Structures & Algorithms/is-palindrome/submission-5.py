class Solution:
    def isPalindrome(self, s: str) -> bool:
        fs = re.sub('[^A-Za-z0-9]', '', s).upper()
        
        l = 0
        r = len(fs)-1
        while l < r:
            print()
            if fs[l] != fs[r]:
                return False
            l+=1
            r-=1

        return True