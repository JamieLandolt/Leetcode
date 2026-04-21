from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        match n:
            case 1:
                return [0, 1]
            case _:
                prev = self.grayCode(n - 1)
                return prev + list(map(lambda x: (x | (1 << n - 1)), reversed(prev.copy())))

s = Solution()
print(s.grayCode(3))