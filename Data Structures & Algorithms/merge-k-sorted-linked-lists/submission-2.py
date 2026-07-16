# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode()
        for l1 in lists:
            l2 = head.next
            cur = ListNode()
            head = cur

            while l1 and l2:
                if l1.val < l2.val:
                    cur.next = l1
                    cur = cur.next
                    l1=l1.next
                else:
                    cur.next = l2
                    cur = cur.next
                    l2=l2.next
            cur.next = l1 if l1 else l2

        
        return head.next