class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0 for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]
        # If same you take the diagonal
        # Else it's the min of surrounding + 1

        #        M  O  V  I  E
        #   [[0, 1, 2, 3, 4, 5]
        # L  [1, 1, 2, 3, 4, 5]
        # O  [2, 2, 1, 2, 3, 4]
        # V  [3, 3, 2, 1, 2, 3]
        # E  [4, 4, 3, 2, 2, 2]]

        for i in range(len(word1) + 1):
            for j in range(len(word2) + 1):
                if i == 0 and j == 0:
                    dp[i][j] = 0
                elif i == 0:
                    dp[i][j] = dp[i][j - 1] + 1
                elif j == 0:
                    dp[i][j] = dp[i - 1][j] + 1
                else:
                    if word1[i - 1] == word2[j - 1]:
                        dp[i][j] = dp[i - 1][j - 1]
                    else:
                        dp[i][j] = min(dp[i - 1][j - 1], min(dp[i][j - 1], dp[i - 1][j])) + 1
        return dp[-1][-1]


