from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Build map
        next_gr = [-1] * 10000

        stack = []
        for num in reversed(nums2):
            print(stack, num)
            while stack and stack[-1] <= num:
                stack.pop()
            if stack:
                next_gr[num] = stack[-1]
            stack.append(num)

        ans = []
        for num in nums1:
            ans.append(next_gr[num])
        return ans
