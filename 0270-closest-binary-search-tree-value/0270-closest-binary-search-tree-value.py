# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: Optional[TreeNode]
        :type target: float
        :rtype: int
        """
        # inorder traversal
        values = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            values.append(node.val)
            inorder(node.right)
        inorder(root)

        # find the closest value using a simple loop
        closest = values[0]
        for val in values:
            if abs(val - target) < abs(closest - target):
                closest = val
        return closest