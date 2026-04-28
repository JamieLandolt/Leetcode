from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for price in range(len(dp)):
            for coin in coins:
                if price - coin >= 0:
                    dp[price] = min(dp[price], dp[price - coin] + 1)

        return dp[-1] if dp[-1] != float('inf') else -1
