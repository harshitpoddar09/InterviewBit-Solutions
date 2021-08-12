# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
 
class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def postorderTraversal(self, A):
        def postorder(A,ans):
            if not A:
                return
            postorder(A.left,ans)
            postorder(A.right,ans)
            ans.append(A.val)
            return ans
        return postorder(A,[])