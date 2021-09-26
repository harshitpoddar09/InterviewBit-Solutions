# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
 
class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        def hasPath(root,arr,x):
            if not root:
                return False
            arr.append(root.val)
            if root.val==x:
                return True
            if hasPath(root.left,arr,x) or hasPath(root.right,arr,x):
                return True
            arr.pop()
            return False
        arr=[]
        if hasPath(A,arr,B):
            return arr