# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        self.res = 0
        def dfs(node):
            if not node:
                return 1
            l = dfs(node.left)
            r= dfs(node.right)
            self.res = max(self.res,abs(l-r))
            return 1 + max(l,r)
        dfs(root)
        return self.res <= 1