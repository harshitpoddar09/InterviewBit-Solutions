# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
 
class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def kthsmallest(self, A, B):
        nodes=[]
        level=[A]
        while level:
            temp=[]
            for cur in level:
                nodes.append(cur.val)
                if cur.left:
                    temp.append(cur.left)
                if cur.right:
                    temp.append(cur.right)
            level=temp
        nodes.sort()
        return nodes[B-1]
