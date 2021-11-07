# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr, linked_list = [], head
        
        while linked_list is not None:
            arr.append(linked_list.val)
            linked_list = linked_list.next
        
        for i in range(1, len(arr) // 2 + 1):
            if arr[i - 1] != arr[-i]:
                return False
        return True