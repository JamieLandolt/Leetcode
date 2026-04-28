from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)

        for i in range(len(s) + 1):
            if i == 0:
                dp[i] = True
                continue

            for word in wordDict:
                pos = i - len(word)
                if pos >= 0 and dp[pos] and word == s[pos:i]:
                    dp[i] = True
        return dp[-1]

