class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        num = 0
        if self.sign(dividend) == self.sign(divisor):
            op = "-"
        else:
            op = "+"

        dividend = self.pos(dividend)
        divisor = self.pos(divisor)
        factor = 2 ** 31 / 2

        if divisor == 1:
            ans = dividend if op == "-" else -dividend
        else:
            while dividend >= divisor:
                if dividend - factor * divisor >= 0:
                    dividend -= factor * divisor
                    num += factor
                factor /= 2

            if op == "+":
                ans = -int(num)
            else:
                ans = int(num)

        if ans >= 2**31:
            ans = 2**31 - 1
        elif ans < -2**31:
            ans = -2**31
        return ans

    def sign(self, x):
        return "-" if str(x)[0] == "-" else "+"

    def pos(self, x):
        return x if x > 0 else -x

s = Solution()
print(s.divide(-2147483648, -1))