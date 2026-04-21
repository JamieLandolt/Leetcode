from math import log
from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        num_bits = [0]
        power_of_2 = lambda x: x > 0 and not x & (x - 1)
        last_power_of_2 = -1
        for i in range(1, n + 1):
            if power_of_2(i):
                num_bits.append(1)
                last_power_of_2 = i
            else:
                num_bits.append(1 + num_bits[i - last_power_of_2])
        return num_bits


