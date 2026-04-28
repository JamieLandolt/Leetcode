class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * (len(nums) + 1)

        for i, num in enumerate(nums):
            for j, subseq_largest in enumerate(nums):
                if j == i:
                    break
                if num > subseq_largest:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
