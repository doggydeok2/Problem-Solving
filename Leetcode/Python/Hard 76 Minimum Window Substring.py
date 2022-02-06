class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = collections.Counter(t)
        need_len = len(t)
        start = end = left = 0
        
        for right, val in enumerate(s, 1):
            need_len -= need[val] > 0
            need[val] -= 1
            
            if need_len == 0:
                while left < right and need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1
            
                if not end or right - left <= end - start:
                    start, end = left, right
                    need[s[left]] += 1
                    need_len += 1
                    left += 1
        return s[start:end]
