# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
            
        current = head.next
        rev_head = head
        rev_head.next = None

        while current!=None:
            print(current.val)
            temp = current
            current = current.next
            temp.next = rev_head
            rev_head = temp
        return rev_head







