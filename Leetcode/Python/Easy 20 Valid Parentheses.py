class Solution:
    def isValid(self, s: str) -> bool:        
        stack = []
        check = True
        try:
            for ch in s:
                if ch == "(" or ch == "{" or ch == "[":
                    stack.append(ch)
                elif ch == ")" and stack.pop() != "(" or ch == "]" and stack.pop() != "[" or ch == "}" and stack.pop() != "{":
                    check = False
                    break
            return True if check and not stack else False
        except:
            return False
