class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []
        def dfs(i, n):
            if i == n - 1:
                output.append(nums[:])
            else:
                for x in range(i, n):
                    nums[x], nums[i] = nums[i], nums[x]
                    dfs(i + 1, n)
                    nums[x], nums[i] = nums[i], nums[x]
        
        dfs(0, len(nums))
        return output

# using itertools
# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         return list(itertools.permutations(nums))