class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        def dfs(arr, idx):
            if idx == len(nums):
                output.append(arr[:])
            else:
                dfs(arr, idx + 1)
                arr.append(nums[idx])
                dfs(arr, idx + 1)
                arr.pop()
        dfs([], 0)
        return output