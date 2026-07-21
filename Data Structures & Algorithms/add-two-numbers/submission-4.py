# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getNum(self, node):
        num = 0
        place = 1
        while node:
            val = node.val * place
            place *= 10
            num += val
            node = node.next
        return num
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1Val = self.getNum(l1)
        l2Val = self.getNum(l2)
        total = l1Val + l2Val

        ret = ListNode()
        cur = ret
        lenTotal = len(str(total))
        for i in range(lenTotal):
            rem = total%10
            total //= 10
            node = ListNode(rem)
            cur.next = node
            cur = cur.next            
            
        return ret.next
            

            
