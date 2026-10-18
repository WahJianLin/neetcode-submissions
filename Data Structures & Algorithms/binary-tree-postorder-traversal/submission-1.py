# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ret = []
        stack = [root]
        visit = {root.val: False}
        while stack:
            cur = stack.pop()
            if cur:
                print(cur.val, visit[cur.val])
                if visit[cur.val]== True:
                    print('yes')
                    ret.append(cur.val)
                else:
                    visit[cur.val] = True
                    stack.append(cur)
                    if cur.right:
                        stack.append(cur.right)
                        visit[cur.right.val] = False
                    if cur.left:
                        stack.append(cur.left)
                        visit[cur.left.val] = False

        print(visit)
        return ret