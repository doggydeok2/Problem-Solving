class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        output = []
        def dfs(arr, i, p):
            if p == k:
                output.append(arr[:])
            elif i == n + 1:
                pass
            else:
                dfs(arr, i + 1, p)
                arr.append(i)
                dfs(arr, i + 1, p + 1)
                arr.pop()

        dfs([], 1, 0)
        return output

# using itertools
# class Solution:
#     def combine(self, n: int, k: int) -> List[List[int]]:
#         return itertools.combinations(range(1, n + 1), k)