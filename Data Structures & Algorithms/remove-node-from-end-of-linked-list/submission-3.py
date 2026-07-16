# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        prev = None
        count = 0 
        while cur:
            count+=1
            cur = cur.next
        if count is n:
            return head.next
        pos = count - n
        count = 1
        cur = head
        while count < pos:
            count+=1
            cur = cur.next

        if cur.next:
            cur.next = cur.next.next
        else:
            head = head.next

        return head
            
