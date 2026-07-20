# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, og: Optional[ListNode]):
        prev = None
        cur = og
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev
    def mergeList(self, l1, l2):
        if not l2:
            return l1
        if not l1:
            return l2
        start = ListNode()
        cur = start
        while l1:
            cur.next = l1
            l1=l1.next
            cur = cur.next
            cur.next = l2
            if l2:
                l2 = l2.next
            cur = cur.next
        return start.next
    def reorderList(self, head: Optional[ListNode]) -> None:        
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        half = slow.next
        slow.next = None
        rev = self.reverseList(half)

        self.mergeList(head, rev)
       


        
            
        



