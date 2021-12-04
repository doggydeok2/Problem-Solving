class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        def dfs(arr, i, acc):
            if acc == target:
                output.append(arr[:])
            for idx in range(i, len(candidates)):
                if acc + candidates[idx] <= target:
                    arr.append(candidates[idx])
                    dfs(arr[:], idx, acc + candidates[idx])
                    arr.pop()
        dfs([], 0, 0)
        return output