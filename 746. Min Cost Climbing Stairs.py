from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0 for i in range(len(cost))]
        for step in range(len(cost)):
            if step == 0:
                dp[step] = cost[step]
            elif step == 1:
                dp[step] = cost[step]
            else:
                dp[step] = cost[step] + min(dp[step - 1], dp[step - 2])
        return min(dp[len(cost) - 1], dp[len(cost) - 2])