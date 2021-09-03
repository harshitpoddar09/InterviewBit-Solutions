# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
 
class Solution:
    # @param A : root node of tree
    # @return the root node in the tree
    def invertTree(self, A):
        def mirror(root):
            if not root:
                return
            temp=root
            mirror(root.left)
            mirror(root.right)
            temp=root.left
            root.left=root.right
            root.right=temp
        mirror(A)
        return A
