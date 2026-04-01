from typing import List


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        times = [0] * 60
        total = 0
        for t in time:
            other = - t % 60
            total += times[other]
            times[t % 60] = times[t % 60] + 1
        return total
