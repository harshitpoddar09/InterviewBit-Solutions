# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
 
class Solution:
    # @param A : tuple of integers
    # @return the root node in the tree
    def sortedArrayToBST(self, A):
        def arrtobst(arr):
            if not arr:
                return None
            mid=len(arr)//2
            root=TreeNode(arr[mid])
            root.left=arrtobst(arr[:mid])
            root.right=arrtobst(arr[mid+1:])
            return root
        return arrtobst(A)
