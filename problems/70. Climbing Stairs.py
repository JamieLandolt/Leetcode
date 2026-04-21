class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0 for i in range(n + 1)]
        for step in range(n + 1):
            if step in (0, 1):
                dp[step] = 1
            else:
                dp[step] = dp[step - 1] + dp[step - 2]
        return dp[n]
