# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
 
class Solution:
    # @param A : root node of tree
    # @return an integer
    def isBalanced(self, A):
        def height(root):
            if not root:
                return 0
            return max(height(root.left),height(root.right))+1
        if not A:
            return 1
        lh=height(A.left)
        rh=height(A.right)
        if abs(lh-rh)<=1 and self.isBalanced(A.right) and self.isBalanced(A.left):
            return 1
        return 0