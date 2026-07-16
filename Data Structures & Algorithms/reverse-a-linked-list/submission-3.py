# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        rev = None
        while current:
            temp = current
            current=current.next
            temp.next = rev
            rev = temp
        return rev





