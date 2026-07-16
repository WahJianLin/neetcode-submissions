# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def least(node):
            if not node:
                return
            
            while node.left:
                node=node.left
            return node

        def remove(node, val):
            if not node:
                return
            
            if val < node.val:
                node.left = remove(node.left, val)
            elif val > node.val:
                node.right = remove(node.right, val)
            else:
                if not node.left and not node.right:
                    return None
                elif not node.left:
                    return node.right
                elif not node.right:
                    return node.left
                else:
                    temp = least(node.right)
                    node.val = temp.val
                    node.right = remove(node.right, temp.val)
            return node

        return remove(root, key)
