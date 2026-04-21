from typing import List


class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        rows = {i: None for i in range(len(grid))}
        for row in grid:
            self.insert(row, rows)

        if any(map(lambda x: x is None, rows.values())):
            return -1

        skips = set()
        grid_set = set(range(len(grid)))
        count = len(grid) - 1
        dist_total = 0

        while skips != grid_set:
            dist = 0
            for i, row in enumerate(grid):
                if i in skips:
                    continue
                if self.get_zeroes(row) >= count:
                    skips.add(i)
                    dist_total += dist
                    count -= 1
                    break
                dist += 1

        return dist_total

    def get_zeroes(self, row):
        count = 0
        for i in range(len(row) - 1, -1, -1):
            if row[i] == 0:
                count += 1
            else:
                return count
        return count

    def insert(self, row, rows):
        count = self.get_zeroes(row)

        for i in range(min(count, len(row) - 1), -1, -1):
            if not rows[i]:
                rows[i] = row
                break

grid = [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]
s = Solution().minSwaps(grid)
print(s)