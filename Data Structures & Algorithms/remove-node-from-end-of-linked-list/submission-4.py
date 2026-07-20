# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        cur = head
        count = 0
        while cur:
            cur = cur.next
            count+=1
        pos = count - 1 - n
        if pos < 0:
            head=head.next
            return head
        cur = head
        count = 0
        while count<pos:
            cur = cur.next
            count+=1
        cur.next = cur.next.next
        return head
            
