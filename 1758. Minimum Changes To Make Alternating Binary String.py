class Solution:
    def minOperations(self, s: str) -> int:
        op1 = "10" * (len(s) // 2 + 1)
        op2 = "01" * (len(s) // 2 + 1)
        return min(sum(map(lambda x: x[0][0] == x[1], zip(zip(op1, op2), s))), sum(map(lambda x: x[0][1] == x[1], zip(zip(op1, op2), s))))

print(Solution().minOperations("10011011"))