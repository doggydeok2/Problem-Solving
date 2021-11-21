class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter, stack = collections.Counter(s), []
        for ch in s:
            counter[ch] -= 1
            if ch in stack:
                continue
            while stack and stack[-1] > ch and counter[stack[-1]] > 0:
                stack.pop()
            stack.append(ch)
        return ''.join(stack)
