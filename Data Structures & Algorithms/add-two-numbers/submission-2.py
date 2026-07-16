# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        c1 = l1
        c2 = l2
        head = ListNode()
        cur = head
        carry = 0
        while c1 or c2 or carry > 0:
            val = carry
            carry =0
            if c1:
                val+=c1.val
                c1 = c1.next
            if c2:
                val+=c2.val
                c2 = c2.next
            if val > 9:
                carry = 1
                val %= 10

            cur.next = ListNode(val)
            cur = cur.next
            
        return head.next
            

            
