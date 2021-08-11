# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
 
class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def inorderTraversal(self, A):
        ans=[]
        def inorder(A,ans):
            if not A:
                return
            inorder(A.left,ans)
            ans.append(A.val)
            inorder(A.right,ans)
            return ans
        return inorder(A,ans)