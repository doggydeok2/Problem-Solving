# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        depth = 1
        q = collections.deque([[root, depth]])
        
        while q:
            popped_root, depth = q.popleft()
            if popped_root.left:
                q.append([popped_root.left, depth + 1])
            if popped_root.right:
                q.append([popped_root.right, depth + 1])
        return depth