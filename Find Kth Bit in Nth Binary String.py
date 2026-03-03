class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        return self.genString(n)[k]

    def genString(self, n):
        match n:
            case 1:
                return "0"
            case _:
                x = self.genString(n - 1)
                return x + "1" + self.invert(x)[::-1]

    def invert(self, y):
        return ''.join((map(lambda x: str(1 - int(x)), y)))

s = Solution()
print(s.genString(20))
