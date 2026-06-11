from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        return list(self.pacific(heights) & self.atlantic(heights))

    def pacific(self, heights: List[List[int]]) -> List[List[int]]:
        blocked = set()
        new_blocked = None
        flow = set()
        while new_blocked != blocked:
            new_blocked = blocked.copy()

            for r in range(len(heights)):
                for c in range(len(heights[0])):
                    if r == 0 or c == 0:
                        flow.add((r, c))
                    elif self.neighbour_flows(r, c, flow, heights):
                        flow.add((r, c))
                        if (r, c) in blocked:
                            blocked.remove((r, c))
                    else:
                        blocked.add((r, c))
        return flow

    def atlantic(self, heights: List[List[int]]) -> List[List[int]]:
        blocked = set()
        new_blocked = None
        flow = set()

        while new_blocked != blocked:
            new_blocked = blocked.copy()

            for r in range(len(heights)):
                for c in range(len(heights[0])):
                    if r == len(heights) - 1 or c == len(heights[0]) - 1:
                        flow.add((r, c))
                    elif self.neighbour_flows(r, c, flow, heights):
                        flow.add((r, c))
                        if (r, c) in blocked:
                            blocked.remove((r, c))
                    else:
                        blocked.add((r, c))
        return flow

    def neighbour_flows(self, r, c, flows, heights):
        for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nb = (r + x, c + y)
            if nb in flows and heights[nb[0]][nb[1]] <= heights[r][c]:
                return True
        return False
