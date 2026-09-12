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
            return

        clones = {}
        d = deque()
        d.append(node)
        while d:
            for i in range(len(d)):
                p = d.popleft()
                newNode = clones[p.val] if p.val in clones else Node(p.val)
                clones[p.val] = newNode
                for n in p.neighbors:
                    if n.val not in clones:
                        d.append(n)
                    nNode = clones[n.val] if n.val in clones else Node(n.val)
                    clones[n.val] = nNode
                    newNode.neighbors.append(nNode)
        return clones[node.val]
