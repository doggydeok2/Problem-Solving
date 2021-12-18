# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    longest = 0
    
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node is None:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            left = left + 1 if node.left and node.left.val == node.val else 0
            right = right + 1 if node.right and node.right.val == node.val else 0
            self.longest = max(self.longest, left + right)
            return max(left, right)
        
        dfs(root)
        return self.longest
        