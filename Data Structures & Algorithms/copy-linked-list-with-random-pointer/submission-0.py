"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cur = head
        start = Node(0)
        crl = start
        kv = {}
        # generates initial list
        while cur:
            node = Node(cur.val)
            crl.next = node
            kv[cur] = node
            cur = cur.next
            crl = crl.next


        cur = head
        crl = start.next

        #generates the random
        while cur:
            if cur.random:
                crl.random = kv[cur.random]
            cur = cur.next
            crl = crl.next
        
        return start.next