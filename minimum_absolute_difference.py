from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        acc = []
        mad = float('inf')
        arr.sort()
        for i in range(len(arr) - 1):
            mad = min(mad, arr[i+1] - arr[i])
        for i in range(len(arr) - 1):
            if arr[i+1] - arr[i] < mad:
                mad = arr[i+1] - arr[i]
                acc = []
            if arr[i+1] - arr[i] == mad:
                acc.append([arr[i], arr[i+1]])
        return acc



s = Solution()
print(s.minimumAbsDifference([4,2,1,3]))