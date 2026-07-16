# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        total = 0
        def find(node, target, total):
            if not node:
                return False
            total += node.val
            if not node.left and not node.right:
                if total == targetSum:
                    return True
                return False
            elif find(node.left, target, total):
                return True
            elif find(node.right, target, total):
                return True
            total -= node.val
            return False       

        return find(root, targetSum, total)