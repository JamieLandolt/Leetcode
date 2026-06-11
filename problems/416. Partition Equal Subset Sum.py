from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False

        dp = [False for _ in range(total // 2 + 1)]  # 0 1 2 3 5678
        dp[0] = True

        for num in nums:  # 5
            for i in range(total // 2, -1, -1):
                if dp[i] and i + num <= total // 2:
                    dp[i + num] = True

        return dp[-1]
