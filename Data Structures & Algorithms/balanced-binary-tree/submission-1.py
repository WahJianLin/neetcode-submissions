# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def bal(node, depth):
            if not node:
                return (True, depth)
            depth += 1
            left = bal(node.left, depth)
            right = bal(node.right, depth)
            if not left[0] or not right[0]:
                return (False, depth)
            diff = abs(left[1] - right[1])
            if diff > 1:
                return (False, depth)
            maximum = max(left[1], right[1])
            return (True, maximum)
        return bal(root, 0)[0]