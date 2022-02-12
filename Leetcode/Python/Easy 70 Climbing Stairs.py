class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        ways = [0] * (n + 1)
        ways[1], ways[2] = 1, 2
        
        for i in range(3, n + 1):
            ways[i] = ways[i - 2] + ways[i - 1]
        return ways[n]
