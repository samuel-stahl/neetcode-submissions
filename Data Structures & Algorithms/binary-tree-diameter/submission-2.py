# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.res = 0

        def helper(node):
            if not node:
                return 0
            height_left = helper(node.left)   
            height_right = helper(node.right)

            if node.left:
                height_left += 1
            if node.right:
                height_right += 1

            max_height = max(height_left, height_right)
            self.res = max(self.res, height_left + height_right)

            return max_height
        
        _ = helper(root)
        return self.res

                