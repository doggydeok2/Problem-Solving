class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(substring, idx):
            if idx == len(digits):
                ans.append(substring)
            else:
                for num_val in num_vals[digits[idx]]:
                    dfs(substring + num_val, idx + 1)
        
        num_vals = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        ans = []
        
        dfs("", 0)
        return ans if len(digits) else []
