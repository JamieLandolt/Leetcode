class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        best = 0
        nums = set(nums)
        for num in nums:
            if num - 1 not in nums: 
                save = num
                while num in nums:
                    num += 1
                best = max(num - save, best)
        return best