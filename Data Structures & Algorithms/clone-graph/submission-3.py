"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        created = {}
        d = deque()
        d.append(node)
        while d:
            for i in range(len(d)):
                target = d.popleft()
                #checks if we already have the node. if not create it
                newNode = created[target.val] if target.val in created else Node(target.val)
                for n in target.neighbors:
                    neighbor = created[n.val] if n.val in created else Node(n.val)
                    newNode.neighbors.append(neighbor)
                    if n.val not in created:
                        d.append(n)
                    created[n.val] = neighbor
                created[newNode.val] = newNode
                
        return created[node.val]
                