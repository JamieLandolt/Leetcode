from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        biggest_window = 0
        window = defaultdict(int)

        while r < len(s):
            if self.any_char_works(r, l, k, window, s):
                window[s[r]] += 1
                r += 1
            else:
                window[s[l]] -= 1
                l += 1
            biggest_window = max(biggest_window, r - l)
        return biggest_window

    def any_char_works(self, r, l, k, window, s):
        if r - l == 0:
            return True
        for char in window:
            if s[r] == char and r - l <= k + window[char] or r - l < k + window[char]:
                return True
        return False

print(Solution().characterReplacement("BAAA", 0))