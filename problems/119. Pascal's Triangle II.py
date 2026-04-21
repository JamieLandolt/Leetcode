from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        return [1] + self.sums(self.getRow(rowIndex - 1)) + [1]

    def sums(self, row: List[int]) -> List[int]:
        sums = []
        for i in range(len(row) - 1):
            sums.append(row[i] + row[i + 1])
        return sums

