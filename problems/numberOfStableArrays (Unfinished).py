from math import comb, perm

class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        total = 0
        length = zero + one

        for arr_size in range(limit, length + 1):
            for num_zeroes in range(1, min(zero + 1, limit)):
                total += comb(arr_size, num_zeroes)
                total %= (10 ** 9 + 7)
        return total

# limit = 3
# [1, 2, 3, 4, 5]

# [1, 2, 3], [2, 3, 4], [3, 4, 5]
# [1, 2, 3, 4], [2, 3, 4, 5]
# [1, 2, 3, 4, 5]

Solution().numberOfStableArrays()