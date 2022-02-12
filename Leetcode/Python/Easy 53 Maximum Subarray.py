class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        output = -20000
        max_sum = -20000
        for num in nums:
            if output < num < 0 or output <= 0 <= num:
                output = num
            else:
                output += num
            max_sum = max(max_sum, output)
        return max_sum
