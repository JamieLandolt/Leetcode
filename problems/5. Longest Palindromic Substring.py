class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[True if r - l == 0 or s[l] == s[r] and r - l == 1 else False for l in range(len(s))
                ] for r in range(len(s))]
        longest = (0, 0)
        longest_size = 1
        for l in range(len(s) - 1, -1, -1):
            for r in range(len(s)):
                if l > r or l == len(s) - 1 or r == 0:
                    continue
                if dp[l + 1][r - 1]:
                    if s[l] == s[r]:
                        dp[l][r] = True
                        if r - l + 1 > longest_size:
                            longest = (l, r)
                            longest_size = r - l + 1
        return s[longest[0] : longest[1] + 1]