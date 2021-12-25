# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return 'null'
        
        q = collections.deque([root])
        encoded = []
        while q:
            popped_node = q.popleft()
            if popped_node:
                q.append(popped_node.left)
                q.append(popped_node.right)
                encoded.append(str(popped_node.val))
            else:
                encoded.append('null')
            
        # while encoded[-1] == 'null':
        #     encoded.pop()
        
        return ','.join(encoded)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        encoded = ['null'] + data.split(',')
        index = 2
        
        if encoded[1] == 'null':
            return []
        root = TreeNode(int(encoded[1]))
        q = collections.deque([root])
        while q and len(encoded) > index:
            popped_node = q.popleft()
            if encoded[index] != 'null':
                popped_node.left = TreeNode(int(encoded[index]))
                q.append(popped_node.left)
            index += 1
            
            if encoded[index] != 'null':
                popped_node.right = TreeNode(int(encoded[index]))
                q.append(popped_node.right)
            index += 1
        
        return root
        
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))