class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        robbed_max = [0] * len(nums)
        robbed_max[0], robbed_max[1] = nums[0], nums[1]
        for i in range(2, len(nums)):
            robbed_max[i] = max(robbed_max[i - 2], robbed_max[i - 3]) + nums[i]
        
        return max(robbed_max[-1], robbed_max[-2])
