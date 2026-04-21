from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.helperRob(nums[1:]), self.helperRob(nums[:-1]))

    def helperRob(self, nums: List[int]) -> int:
        dp = [0 for _ in range(len(nums))]
        for i, cost in enumerate(nums):
            if i in (0, 1):
                dp[i] = cost
            elif i == 2:
                dp[i] = dp[i - 2] + cost
            else:
                dp[i] = cost + max(dp[i - 2], dp[i - 3])
        return max(dp[i - 1], dp[i])
