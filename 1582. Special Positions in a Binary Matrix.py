from typing import List

import numpy as np


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        mat_T = np.transpose(np.array(mat))
        row_1s = {}
        col_1s = {}
        for ri, row in enumerate(mat):
            for pi, pos in enumerate(row):
                if pos == 1:
                    row_1s[ri] = row_1s.get(ri, [])
                    row_1s[ri].append(pi)
                    col_1s[pi] = col_1s.get(pi, [])
                    col_1s[pi].append(ri)

        for k, v in list(row_1s.items()).copy():
            if len(v) > 1:
                for i in v:
                    col_1s.pop(i, None)
                row_1s.pop(k)

        for k, v in list(col_1s.items()).copy():
            if len(v) > 1:
                for i in v:
                    row_1s.pop(i, None)
                col_1s.pop(k)

        return min(len(row_1s), len(col_1s))


print(
        Solution().numSpecial(
            [[0, 0, 0, 0, 0, 1, 0, 0],
             [0, 0, 0, 0, 1, 0, 0, 1],
             [0, 0, 0, 0, 1, 0, 0, 0],
             [1, 0, 0, 0, 1, 0, 0, 0],
             [0, 0, 1, 1, 0, 0, 0, 0]]        )
)