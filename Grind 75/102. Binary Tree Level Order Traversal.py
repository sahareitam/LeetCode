# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        queue = deque()
        queue.append(root)
        res = []

        while queue:
            lvl = []
            size = len(queue)
            for i in range(size):
                if not queue:
                    return res
                cur = queue.popleft()
                if cur:
                    queue.append(cur.left)
                    queue.append(cur.right)
                    lvl.append(cur.val)
            if lvl:
                res.append(lvl)

        return res
