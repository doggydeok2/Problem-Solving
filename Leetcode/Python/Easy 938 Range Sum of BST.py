# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root is None:
            return 0
        
        left_val = self.rangeSumBST(root.left, low, high)
        right_val = self.rangeSumBST(root.right, low, high)
        
        return left_val + right_val + (root.val if low <= root.val <= high else 0)