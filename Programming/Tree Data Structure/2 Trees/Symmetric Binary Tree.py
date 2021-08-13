# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
 
class Solution:
    # @param A : root node of tree
    # @return an integer
    def isSymmetric(self, A):
        def isMirror(a,b):
            if not a and not b:
                return True
            if a and b:
                if a.val==b.val:
                    return isMirror(a.right,b.left) and isMirror(a.left,b.right)
            return False
        if isMirror(A,A):
            return 1
        return 0