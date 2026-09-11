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
        seen = set()
        clones = {}
        def dfs(cur: Optional['Node']):
            if not cur:
                return
            seen.add(cur.val)
            newNode = Node(cur.val) if cur.val not in clones else clones[cur.val]
            newNeighbors = newNode.neighbors if newNode.neighbors else []
            for n in cur.neighbors:
                nNode = Node(n.val) if n.val not in clones else clones[n.val]
                clones[n.val] = nNode
                newNeighbors.append(nNode)
            newNode.neighbors=newNeighbors
            clones[cur.val] = newNode
            for n in cur.neighbors:
                if n.val not in seen:
                    dfs(n)
        
        dfs(node)
        return clones[node.val]
