class Solution:
    def trap(self, height: List[int]) -> int:
        saved_water, left, right = 0, 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        
        while left < right:
            left_max, right_max = max(left_max, height[left]), max(right_max, height[right])
            
            if left_max <= right_max:
                saved_water += left_max - height[left]
                left += 1
            else:
                saved_water += right_max - height[right]
                right -= 1
            
        return saved_water
