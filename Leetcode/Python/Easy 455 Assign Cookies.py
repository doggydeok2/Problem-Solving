class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(reverse=True)
        s.sort(reverse=True)
        cnt = c_idx = 0
        
        for cookie in s:
            while c_idx < len(g) and g[c_idx] > cookie:
                c_idx += 1
            if c_idx == len(g):
                break
            cnt += 1
            c_idx += 1
        return cnt