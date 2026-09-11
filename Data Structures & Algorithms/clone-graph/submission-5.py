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
        def dfs(cur: Optional['Node']):
            if not cur:
                return
            newNode = Node(cur.val)
            clones[cur.val] = newNode
            for n in cur.neighbors:
                nNode = clones[n.val] if n.val in clones else dfs(n)
                newNode.neighbors.append(nNode)
            return newNode

                
        
        dfs(node)
        return clones[node.val]
