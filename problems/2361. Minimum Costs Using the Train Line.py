class Solution:
    def minCosts(self, regular, express, expressCost):
        dp = [[0, 0] for _ in range(len(regular) + 1)]

        for i in range(len(regular) + 1):
            if i == 0:
                continue
            dp[i][0] = min(dp[i - 1][0], dp[i - 1][1]) + regular[i] # 1 indexed
            dp[i][1] = min(dp[i - 1][0] + expressCost, dp[i - 1][1]) + express[i] # 1 indexed
        return list(map(min, dp))