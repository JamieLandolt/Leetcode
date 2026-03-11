from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen_next = {}
        seen = set()
        chain_beginnings = set()
        for i in nums:
            if i + 1 in seen:
                seen_next[i] = {True}
                chain_beginnings.remove(i + 1)
            else:
                seen.add(i)
            chain_beginnings.add(i)
        total = 0
        for i in list(chain_beginnings):
            total = max(total, self.count_length(i, seen_next))
        return total

    def count_length(self, num, seen_next):
        total = 0
        while num + 1 in seen_next:
            total += 1
            num += 1
        return total
