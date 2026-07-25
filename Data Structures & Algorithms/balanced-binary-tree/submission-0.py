# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def height(self, node, depth):
        if not node:
            return 0
        left = self.height(node.left, depth)
        right = self.height(node.right, depth)
        return max(left, right) + 1
    def isBal(self, root: Optional[TreeNode],depth) -> bool:
        ret = True
        if not root:
            return ret
        
        lBal = self.isBal(root.left, depth)
        rBal = self.isBal(root.right,depth)
        if not lBal or not rBal:
            return False
        lHeight = self.height(root.left, depth)
        rHeight = self.height(root.right, depth)
        diff = max(lHeight, rHeight) - min(lHeight,rHeight)
        if diff > 1:
            return False
        return ret
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        depth = 0
        return self.isBal(root, depth)
    