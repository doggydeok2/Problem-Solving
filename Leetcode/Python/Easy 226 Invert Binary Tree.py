# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root
        q = collections.deque([root])
        
        while q:
            for _ in range(len(q)):
                cur_root = q.popleft()
                cur_root.left, cur_root.right = cur_root.right, cur_root.left
                
                if cur_root.left:
                    q.append(cur_root.left)
                if cur_root.right:
                    q.append(cur_root.right)
                
        return root