# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        self.balanced = True

        def helper(node):
            if not node or not self.balanced:
                return 0
            left = helper(node.left)
            right = helper(node.right)

            left = left + 1 if node.left else left
            right = right + 1 if node.right else right

            diff = left - right
            if diff > 1 or diff < -1:
                self.balanced = False

            return max(left, right)

        helper(root)
        return self.balanced


        