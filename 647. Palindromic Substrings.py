class Solution:
    def countSubstrings(self, s: str) -> int:
        total = 0
        for pos in range(len(s)):
            total += self.expand(s, pos)
        return total

    def expand(self, s, i):
        count = 1  # Account for singleton palindrome
        if i != len(s) - 1:
            l, r = i, i + 1

            while l >= 0 and r < len(s) and s[l] == s[r]:
                print(0, s[l], s[r])
                count += 1
                l -= 1
                r += 1

        l, r = i - 1, i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            print(1, s[l], s[r])
            count += 1
            l -= 1
            r += 1
        return count

Solution().countSubstrings("aaa")