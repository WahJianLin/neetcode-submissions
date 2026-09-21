class Solution:
    def reverseBits(self, n: int) -> int:
        rev = 0
        for i in range(32):
            rev = rev << 1
            if n&1 == 1:
                rev+=1
            n = n >> 1

        return rev