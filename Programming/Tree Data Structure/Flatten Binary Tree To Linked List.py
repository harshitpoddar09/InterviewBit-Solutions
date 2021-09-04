# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
 
class Solution:
    # @param A : root node of tree
    # @return the root node in the tree
    def flatten(self, A):
        traverse=[]
        def preorder(A,traverse):
            if not A:
                return 
            traverse.append(A.val)
            preorder(A.left,traverse)
            preorder(A.right,traverse)
            return traverse
        a=preorder(A,traverse)
        root=TreeNode(a[0])
        ans=root
        for i in range(1,len(a)):
            root.right=TreeNode(a[i])
            root=root.right
        return ans