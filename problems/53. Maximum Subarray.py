class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        max_left = 0
        for num in nums:
            ans = max(max_left + num, ans)
            max_left = max(0,  max_left + num)
        return ans
