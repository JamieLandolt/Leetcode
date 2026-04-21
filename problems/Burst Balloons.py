from typing import List


class Solution:
    cache = {}

    def maxCoins(self, nums: List[int], removed=0) -> int:
        if removed == 2 ** len(nums) - 1:
            return 0

        scores = []
        nums = tuple(nums)
        for i in range(len(nums)):
            if (removed >> i) % 2 == 1:
                continue
            score = self.getCoins(nums, i - 1) * self.getCoins(nums, i) * self.getCoins(nums, i + 1)

            new_removed = removed | 2 ** i
            if removed in self.cache:
                subscore = self.cache[new_removed]
            else:
                subscore = self.maxCoins(nums, new_removed)
                self.cache[new_removed] = subscore
            scores.append(score + subscore)
        return max(scores)

    def getCoins(self, nums, i):
        if 0 <= i < len(nums):
            return nums[i]
        return 1

print(Solution().maxCoins([3, 1, 5, 8]))