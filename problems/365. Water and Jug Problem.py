class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        if 0 > target or target > x + y:
            return False
        
        dp = [False for _ in range(x + y + 1)]
        dp[0] = True
        new = [0]
        seen = set()

        while len(new) > 0:
            num = new.pop()
            
            if num in seen:
                continue
            seen.add(num)
                
            if num <= y:
                dp[x + num] = True
                new.append(x + num)
            if num <= x:
                dp[y + num] = True
                new.append(y + num)
            if 0 <= y - (x - num) <= x + y:
                dp[y - (x - num)] = True
                new.append(y - (x - num))
            if 0 <= x - (y - num) <= x + y:
                dp[x - (y - num)] = True
                new.append(x - (y - num))

        return dp[target]
        
