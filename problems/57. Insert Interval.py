from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        return self.merge(intervals)

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        i = 0
        n = len(intervals)
        intervals.sort()

        while i < n - 1:
            if intervals[i][1] >= intervals[i + 1][0]:
                intervals[i][1] = max(intervals[i + 1][1], intervals[i][1])
                intervals.pop(i + 1)
                n -= 1
            else:
                i += 1
        return intervals