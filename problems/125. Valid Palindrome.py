class Solution(object):
    def isPalindrome(self, s):
        l, r = 0, len(s) - 1

        while l < r:
            while not s[l].isalnum() and l != r:
                l += 1
            while not s[r].isalnum() and l != r:
                r -= 1
            if l == r:
                break
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1

        if len(s) % 2 == 1:
            return s[l] == s[r]
        return True

