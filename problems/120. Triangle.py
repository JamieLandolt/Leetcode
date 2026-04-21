from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        cache = {}
        return self.min(triangle, 0, 0, cache)

    def min(self, triangle, r, c, cache):
        if r == len(triangle):
            return 0

        left = cache.get((r + 1, c), None)
        if left is None:
            left = self.min(triangle, r + 1, c, cache)
            cache[(r + 1, c)] = left
        right = cache.get((r + 1, c + 1), None)
        if right is None:
            right = self.min(triangle, r + 1, c + 1, cache)
            cache[(r + 1, c + 1)] = right

        return triangle[r][c] + min(left, right)
