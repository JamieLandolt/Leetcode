from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}
        return self.robPerm(nums, 0, cache)

    def robPerm(self, nums, i, cache):
        if i >= len(nums):
            return 0

        cur = cache.get(i + 1, None)
        if cur is None:
            cur = self.robPerm(nums, i + 1, cache)
            cache[i + 1] = cur
        nex = cache.get(i + 2, None)
        if nex is None:
            nex = self.robPerm(nums, i + 2, cache)
            cache[i + 2] = nex

        return max(nums[i] + nex, cur)
