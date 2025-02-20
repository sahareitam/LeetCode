# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        l1 = [root]
        l2 = [root]
        node = root

        while p != node:
            if p.val > node.val:
                l1.append(node.right)
                node = node.right
            else:
                l1.append(node.left)
                node = node.left

        node = root
        while q != node:
            if q.val > node.val:
                l2.append(node.right)
                node = node.right
            else:
                l2.append(node.left)
                node = node.left
        anc = None
        for i1, i2 in zip(l1, l2):
            if i1.val == i2.val:
                anc = i1

        return anc