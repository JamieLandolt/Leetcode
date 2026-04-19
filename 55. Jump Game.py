from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_reachable = len(nums) - 1
        pos = len(nums) - 1
        while pos > 0:
            pos -= 1
            if last_reachable - pos <= nums[pos]:
                last_reachable = pos
        return last_reachable == 0

