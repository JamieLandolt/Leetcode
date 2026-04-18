from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        best = 0
        for i, price in enumerate(prices):
            if price < buy:
                buy = price
            best = max(best, price - buy)
        return best
