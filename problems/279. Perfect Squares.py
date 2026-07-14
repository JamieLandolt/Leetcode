class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0 for _ in range(n + 1)]

        for num in range(1, n + 1):
            perf = []
            for i in range(1, int(num ** 0.5 + 1)):
                perf.append(dp[num - i ** 2])
            dp[num] = min(perf) + 1

        return dp[-1]
