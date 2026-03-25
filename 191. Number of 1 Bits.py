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

[
    [20,17,9 ,13,5 ,2 ,9 ,1 ,5 ],
    [14,9 ,9 ,9 ,16,18,3 ,4 ,12],
    [18,15,10,20,19,20,15,12,11],
    [19,16,19,18,8 ,13,15,14,11],
    [4 ,19,5 ,2 ,19,17,7 ,2 ,2 ]]