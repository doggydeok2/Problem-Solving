# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        backup, node = None, head
        
        while node:
            backup, node.next = node.next, backup
            backup, node = node, backup
        
        return backup