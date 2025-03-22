# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def dfs(node,l,r):
            if not node:
                return True
            if node.val <= l or node.val >= r:
                return False
            return dfs(node.left,l,min(node.val,r)) and dfs(node.right,max(node.val,l),r)
        return dfs(root,float('-inf'),float('inf'))