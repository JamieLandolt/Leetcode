class Solution:
    def myPow(self, x: float, n: int) -> float:
        if str(n)[0] == "-":
            return 1 / self.myPowPos(x, abs(n))
        return self.myPowPos(x, n)

    def myPowPos(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        return self.myPowPos(x * x, n // 2) * self.myPowPos(x, n % 2)