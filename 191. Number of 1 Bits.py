class Solution:
    def hammingWeight(self, n: int) -> int:
        i = 0
        while 2 ** i <= n:
            last = i
            i += 1

        count = 0
        for i in range(last, -1, -1):
            x = n - 2 ** i
            if x >= 0:
                n = x
                count += 1
        return count

print(Solution().hammingWeight(128))
