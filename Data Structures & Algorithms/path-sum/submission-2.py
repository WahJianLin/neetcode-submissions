# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, targetSum, val):
            if not node:
                return False
            val += node.val
            if val == targetSum and not node.left and not node.right:
                return True
            if node.left:
                if dfs(node.left,targetSum,val):
                    return True
            if node.right:
                if dfs(node.right,targetSum,val):
                    return True
            val -= node.val
            return False
        return dfs(root, targetSum, 0)
            