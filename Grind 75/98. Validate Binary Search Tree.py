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

        def rec(node, left, right):
            if not node:
                return True
            elif node.val <= left or node.val >= right:
                return False

            return rec(node.left, left, max(node.val, left)) and rec(node.right, min(node.val, right), right)

        return rec(root, float('-inf'), float('inf'))