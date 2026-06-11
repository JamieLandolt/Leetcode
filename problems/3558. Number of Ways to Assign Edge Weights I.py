import math
from typing import List


class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        self.cache = [1]
        self.tree = {}
        # Build tree
        for u, v in edges:
            smaller, larger = min(u, v), max(u, v)
            if smaller in self.tree:
                self.tree[smaller].append(larger)
            else:
                self.tree[smaller] = [larger]

        # Calc depth and num assignments
        n = self.depth(1)
        return 2 ** (n - 1) % (10 ** 9 + 7)

    def depth(self, node):
        if node not in self.tree:
            return 0
        return 1 + max(self.depth(child) for child in self.tree[node])