class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = []
        for char in s:
            if char.isalnum():
                chars.append(char.lower())
        
        l = len(chars)
        for i in range(l // 2):
            if not chars[i] == chars[-(i + 1)]: return False
        return True

# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         s = s.lower()
#         s = re.sub('[^a-z0-9]', '', s)
#         return s == s[::-1]
