from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = self.filter_pts(points)
        print(points)
        points.sort()
        last_num = - 2 ** 31 - 1
        arrows = 0
        for interval in points:
            if interval[0] <= last_num:
                continue
            last_num = interval[1]
            arrows += 1
        return arrows

    def filter_pts(self, pts):
        pts.sort(key=lambda x: x[1])
        points = []
        for i, interval in enumerate(pts):
            if i == 0:
                points.append(interval)
            if interval[0] > points[-1][0]:
                points.append(interval)
        return points
