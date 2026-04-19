from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy_price = float('inf')
        for i in range(len(prices) - 1):
            if prices[i + 1] < prices[i]:
                liquidation = prices[i] - buy_price
                if liquidation > 0:
                    profit += liquidation
                    buy_price = float('inf')
            else:
                buy_price = min(buy_price, prices[i])
        profit += max(0, prices[-1] - buy_price)
        return profit
