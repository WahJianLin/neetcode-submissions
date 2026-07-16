class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        a1 = [0]*26
        a2 = [0]*26
        len1 = len(s1)
        l=0

        for c in s1:
            spot = ord(c)-ord('a')
            count = a1[spot]+1
            a1[spot]=count


        for r in range(len(s2)):
            
            spot = ord(s2[r])-ord('a')
            count = a2[spot]+1
            a2[spot]=count
            if r-l+1 > len1:
                spot2 = ord(s2[l])-ord('a')
                count2 = a2[spot2]-1
                a2[spot2]=count2
                l+=1
            if a1==a2:
                return True
        return False