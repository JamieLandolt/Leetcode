"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda x: (x.start, x.end))
        rooms = 0
        next_room = []
        while intervals:
            l, r = 0, 1
            rooms += 1
            next_room = []
            while l < len(intervals) - 1 and r < len(intervals):
                cur = intervals[l]
                nex = intervals[r]
                if cur.end > nex.start:
                    next_room.append(nex)
                    r += 1
                else:
                    l = r
                    r += 1
            intervals = next_room
        return rooms

