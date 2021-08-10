# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
 
class Solution:
    # @param A : root node of tree
    # @return an integer
    def maxDepth(self, A):
        if not A:
            return 0
        ldepth=self.maxDepth(A.left)
        rdepth=self.maxDepth(A.right)
        return max(ldepth,rdepth)+1
