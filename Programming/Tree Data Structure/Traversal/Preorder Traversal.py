# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
 
class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def preorderTraversal(self, A):
        ans=[]
        def preorder(A,ans):
            if not A:
                return 
            ans.append(A.val)
            preorder(A.left,ans)
            preorder(A.right,ans)
            return ans
        return preorder(A,ans)