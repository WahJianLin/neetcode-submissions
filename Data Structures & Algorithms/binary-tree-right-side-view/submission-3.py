# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ret = []
        if not root:
            return []
        q = deque()
        q.append(root)
        while q:
            ql = len(q)
            for i in range(ql):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                if i == ql -1: #reaches the end of the queue
                    ret.append(node.val)
        return ret