# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ret = []
        if not root:
            return ret
        d = deque()
        d.append(root)

        while d:
            size = len(d)
            level = []
            for i in range(size):
                temp = d.popleft()
                if temp:
                    level.append(temp.val)
                    if temp.left:
                        d.append(temp.left)
                    if temp.right:
                        d.append(temp.right)
            ret.append(level)

        return ret