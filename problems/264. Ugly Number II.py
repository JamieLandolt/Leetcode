from collections import deque

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        l1, l2, l3 = deque([1]), deque([1]), deque([1])
        for i in range(2, n + 1):
            next_ugly = min(2 * l1[0], 3 * l2[0], 5 * l3[0])

            if next_ugly == 2 * l1[0]:
                l1.popleft()
            if next_ugly == 3 * l2[0]:
                l2.popleft()
            if next_ugly == 5 * l3[0]:
                l3.popleft()

            l1.append(next_ugly)
            l2.append(next_ugly)
            l3.append(next_ugly)

        return l1[-1]
