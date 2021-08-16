# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
 
class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def solve(self, root):
        def height(root):
            if not root:
                return 0
            lheight=height(root.left)
            rheight=height(root.right)
            if lheight>rheight:
                return lheight+1
            else:
                return rheight+1
        def curLevel(root,level,ans):
            if not root:
                return 
            if level==1:
                ans.append(root.val)
            elif level>1:
                curLevel(root.left,level-1,ans)
                curLevel(root.right,level-1,ans)
            return ans
        h=height(root)
        res=[]
        for i in range(h,0,-1):
            res+=curLevel(root,i,[])
        return res