from typing import List


class Solution:
    def nextCell(self):
        x, y = self.dirs[self.dir_ix]
        r, c = self.pos
        return x + r, y + c

    def dist(self):
        r, c = self.pos
        return r ** 2 + c ** 2

    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        self.dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        self.dir_ix = 0
        self.pos = (0, 0)
        max_dist = 0

        # make a set of tuples (lists are not hashable)
        obstacles = set(map(tuple, obstacles))

        # handle movements + rotations
        for cmd in commands:
            match cmd:
                case -2:
                    self.dir_ix = (self.dir_ix - 1) % 4
                case -1:
                    self.dir_ix = (self.dir_ix + 1) % 4
                case k:
                    # Walk forward until obstacle or steps exhausted
                    i = 0
                    while i < k and (nc := self.nextCell()) not in obstacles:
                        self.pos = nc
                        print(self.pos)
                        i += 1
                    max_dist = max(max_dist, self.dist())
        return max_dist
