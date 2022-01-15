class Solution:
    def search(self, nums: List[int], target: int) -> int:  # nums : [4, 5, 6, 7, 0, 1, 2]
        pivot = nums.index(min(nums))

        l, r = 0, len(nums) - 1
        while l <= r:  # [0, 1, 2, 4, 5, 6, 7]
            m = (l + r) // 2
            actual_m = (pivot + m) % len(nums)
            if nums[actual_m] == target:
                return actual_m
            elif nums[actual_m] > target:
                r = m - 1
            else:
                l = m + 1
        return -1
            