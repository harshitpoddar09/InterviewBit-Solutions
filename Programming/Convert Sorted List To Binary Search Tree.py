# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
 
class Solution:
    # @param A : head node of linked list
    # @return the root node in the tree
    def sortedListToBST(self, A):
        nodes=[]
        while A:
            nodes.append(A.val)
            A=A.next
        def arrtobst(arr):
            if not arr:
                return None
            mid=len(arr)//2
            root=TreeNode(arr[mid])
            root.left=arrtobst(arr[:mid])
            root.right=arrtobst(arr[mid+1:])
            return root
        return arrtobst(nodes)