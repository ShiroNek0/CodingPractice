# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.checkDepth(root)

    def checkDepth(self, input: Optional[TreeNode]) -> int:
        if input is None:
            return 0

        maxSubDepth = max(self.checkDepth(input.left), self.checkDepth(input.right))
        return 1 + maxSubDepth