class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = {}
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = t[i]
            else:
                if d[s[i]] != t[i]:
                    return False

        d = {}
        for i in range(len(s)):
            if t[i] not in d:
                d[t[i]] = s[i]
            else:
                if d[t[i]] != s[i]:
                    return False

        return True