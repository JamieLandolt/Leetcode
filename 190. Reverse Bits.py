class Solution:
    def reverseBits(self, n: int) -> int:
        num = 0
        for i in range(32):
            bit = 1 if (1 << i) & n else 0
            num |= (bit << 31 - i)
        return num