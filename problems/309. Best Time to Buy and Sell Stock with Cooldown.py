from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0, -prices[0], float('-inf')] for _ in range(len(prices) + 1)]

        for i, price in enumerate(prices):
            i += 1
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][2])
            dp[i][1] = max(dp[i - 1][0] - price, dp[i - 1][1])
            dp[i][2] = dp[i - 1][1] + price
        return max(dp[-1])