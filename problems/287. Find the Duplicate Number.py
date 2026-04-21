from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while slow != fast or slow == 0:
            slow = nums[slow] # 3 2
            fast = nums[nums[fast]] # 2 2

        snd_slow = 0
        while snd_slow != slow:
            snd_slow = nums[snd_slow]
            slow = nums[slow]
        return snd_slow
