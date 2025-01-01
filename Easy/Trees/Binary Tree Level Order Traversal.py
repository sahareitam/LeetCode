# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        stack1 = []
        stack2 = []
        stack1.append(root)
        if root == None:
            return []
        while len(stack1) + len(stack2) != 0:
            level = []
            while len(stack1) != 0:
                cur_node = stack1.pop()
                level.append(cur_node.val)
                if cur_node.left != None:
                    stack2.append(cur_node.left)
                if cur_node.right != None:
                    stack2.append(cur_node.right)

            while len(stack2) != 0:
                temp = stack2.pop()
                stack1.append(temp)
            res.append(level)
        return res