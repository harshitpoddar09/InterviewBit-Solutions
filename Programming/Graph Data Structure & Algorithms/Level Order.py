# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
 
class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def levelOrder(self, root):
        ans=[]
        if not root:
            return []
        level=[root]
        while level:
            ans.append([node.val for node in level])
            temp=[]
            for node in level:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            level=temp
        return ans