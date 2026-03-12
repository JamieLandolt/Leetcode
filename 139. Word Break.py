from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str], start=0) -> bool:
        wordDict = set(wordDict)
        found = False
        word = ""
        for i in range(len(s)):
            if found:
                return True
            if i + start == len(s):
                return True if not word or word in wordDict else False
            word += s[i + start]
            if word in wordDict:
                found = max(self.wordBreak(s, wordDict, i + start + 1), found)
        if word in wordDict:
            return True
        return found

print(Solution().wordBreak("applepenapple", ["apple","pen"]))