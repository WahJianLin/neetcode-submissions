class Solution:
    def countBits(self, n: int) -> List[int]:
        ret = [0]*(n+1)
        
        def count1s(num):
            count = 0
            while num > 0:
                if num & 1 ==1:
                    count+=1
                num = num >> 1
            return count
        for i in range(n+1):
            ret[i] = count1s(i)


        return ret