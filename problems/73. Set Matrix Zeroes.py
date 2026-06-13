from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = {}
        cols = {}
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                rows[r] = 0 if rows.get(r, 1) == 0 or matrix[r][c] == 0 else 1
                cols[c] = 0 if cols.get(c, 1) == 0 or matrix[r][c] == 0 else 1
        print(rows)
        print(cols)

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if rows[r] == 0 or cols[c] == 0:
                    matrix[r][c] = 0
