from typing import List

# Recursive + Memoization
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

# DP
class DPSolution:
    def rob(self, nums: List[int]) -> int:
        dp = [0 for _ in range(len(nums))]
        for i, cost in enumerate(nums):
            if i in (0, 1):
                dp[i] = cost
            elif i == 2:
                dp[i] = dp[i - 2] + cost
            else:
                dp[i] = cost + max(dp[i - 2], dp[i - 3])
        print(dp)
        return max(dp[i - 1], dp[i])
