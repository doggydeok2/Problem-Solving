# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        merged_list = ListNode()
        initial = merged_list
        
        while l1 and l2:
            if l1.val >= l2.val:
                merged_list.next = l2
                l2 = l2.next
            else:
                merged_list.next = l1
                l1 = l1.next
            merged_list = merged_list.next
        
        merged_list.next = l1 if l1 else l2
        return initial.next