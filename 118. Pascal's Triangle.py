from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        prev = self.generate(numRows - 1)
        return prev + [[1] + self.sums(prev[-1]) + [1]]

    def sums(self, row: List[int]) -> List[int]:
        sums = []
        for i in range(len(row) - 1):
            sums.append(row[i] + row[i + 1])
        return sums
