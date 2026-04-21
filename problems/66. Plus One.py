from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        if digits[i] == 9:
            while digits[i] == 9:
                digits[i] = 0
                i -= 1
            if digits[0] == 0:
                digits = [1] + digits
            else:
                digits[i] += 1
        else:
            digits[i] += 1
        return digits