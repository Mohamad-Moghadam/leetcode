# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def hasPathSum(self, root, targetSum):
        if root:
            targetSum -= root.val
            if not (root.left) and not (root.right) and targetSum == 0:
                return True
            left_has = self.hasPathSum(root.left, targetSum) if root.left else False
            right_has = self.hasPathSum(root.right, targetSum) if root.right else False
            return left_has or right_has
        else:
            return False
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        
