# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def ismirror(node1,node2):
            if node1 == None and node2 == None:
                return True
            if node1 == None or node2 == None:
                return False
            return node1.val == node2.val and ismirror(node1.left,node2.right) and ismirror(node1.right,node2.left)
        return ismirror(root.left,root.right)
