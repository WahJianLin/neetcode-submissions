# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        temp = slow
        slow = slow.next
        temp.next = None

        rev = None
        while slow:
            temp = slow
            slow =slow.next
            temp.next = rev
            rev = temp
        prev = ListNode()
        cur = head
        while cur:
            temp = cur
            cur = cur.next 
            prev.next =  temp
            prev=prev.next
            if rev:
                temp = rev
                rev = rev.next
                prev.next = temp
                prev=prev.next

        
            
        



