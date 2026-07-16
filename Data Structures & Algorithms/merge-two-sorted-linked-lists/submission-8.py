# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        current = head
        while list1 and list2:
            temp = None
            if list1.val < list2.val:
                temp = list1
                list1=list1.next
            else:
                temp = list2
                list2=list2.next
            current.next = temp
            current = current.next
        if list1:
            current.next = list1
        else:
            current.next = list2
        return head.next