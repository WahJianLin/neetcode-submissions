# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
        head = None
        if list1 is None:
            head = list2
            list2 = list2.next
        elif list2 is None:
            head = list1
            list1 = list1.next
        elif list1.val<list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next
        current = head

        while list1 is not None and list2 is not None:
            if list1.val<list2.val:
                current.next = list1
                list1 =list1.next
            else:
                current.next = list2
                list2 =list2.next
            current = current.next
        if list1 is None:
            current.next = list2
        else:
            current.next = list1



        return head