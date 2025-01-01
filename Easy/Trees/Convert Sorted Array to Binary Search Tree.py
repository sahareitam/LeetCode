# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def createtree(l, r):
            if l > r:
                return
            mid = (l + r) // 2
            root = TreeNode(nums[mid])
            root.left = createtree(l, mid - 1)
            root.right = createtree(mid + 1, r)
            return root

        n = len(nums)
        return createtree(0, n - 1)