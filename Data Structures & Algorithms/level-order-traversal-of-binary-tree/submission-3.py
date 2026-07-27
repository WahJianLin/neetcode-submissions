# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ret = []
        queue = deque()
        queue.append(root)
        while queue:
            level = []
            print(len(queue))
            for i in range(len(queue)):
                node = queue.popleft()
                if node:
                    level.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            if level:
                ret.append(level)
        return ret
