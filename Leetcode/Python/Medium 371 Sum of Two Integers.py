class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFF
        INT_MAX = 0x7FFF
        
        while b != 0:
            a, b = (a ^ b) & MASK, ((a & b) << 1) & MASK
        
        return a if a <= INT_MAX else ~(a ^ MASK)
