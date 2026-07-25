# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeast(self, node: Optional[TreeNode]):
        cur = node
        while cur and cur.left:
            cur = cur.left
        return cur

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.right:
                root = root.left
            elif not root.left:
                root = root.right
            else:
                smallest = self.findLeast(root.right)
                root.val = smallest.val
                root.right = self.deleteNode(root.right, smallest.val)
        return root