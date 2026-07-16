# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1v = self.toNum(l1)
        l2v = self.toNum(l2)
        total = l1v + l2v
        print(l1v, l2v,total)
        head = ListNode()
        cur = head
        while total>0:
            val = total % 10
            total//=10
            node = ListNode(val)
            cur.next = node
            cur = cur.next
        return head.next if head.next else ListNode(0)

    def toNum(self, l:Optional[ListNode]) -> int:
        ret = 0
        mul = 1
        while l:
            val = l.val*mul
            mul*=10
            ret+=val
            l=l.next
        return ret