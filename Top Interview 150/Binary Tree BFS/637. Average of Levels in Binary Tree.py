# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        dic = {}
        res = []

        def avr(node, level):
            if node is None:
                return

            if level in dic:
                dic[level][0] += 1
                dic[level][1] += node.val
            else:
                dic[level] = [1, node.val]

            avr(node.left, level + 1)
            avr(node.right, level + 1)

        avr(root, 0)
        for i in dic:
            res.append(dic[i][1] / dic[i][0])

        return res



