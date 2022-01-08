# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        finished_root = ListNode(-5001)
        finished = finished_root
        while head:
            if head and head.val < finished.val:
                finished = finished_root
            while finished.next and finished.next.val < head.val:
                finished = finished.next
            head, finished.next, finished.next.next = head.next, head, finished.next
        return finished_root.next
        