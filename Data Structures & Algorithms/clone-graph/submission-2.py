"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        created = {}
        
        def dfs(node):
            if not node:
                return
            newNode = Node(node.val)
            created[node.val] = newNode

            for n in node.neighbors:
                nNode = created[n.val] if n.val in created else dfs(n)
                newNode.neighbors.append(nNode)
            
            return newNode

        return dfs(node)
                