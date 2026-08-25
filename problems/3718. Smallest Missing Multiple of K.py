class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums = set(nums)
        mults = k
        while True:
            if mults not in nums:
                return mults
            mults += k

