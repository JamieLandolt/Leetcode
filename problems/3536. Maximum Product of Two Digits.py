class Solution:
    def maxProduct(self, n: int) -> int:
        x = sorted(str(n), reverse=True)[:2]
        return int(x[0]) * int(x[1])