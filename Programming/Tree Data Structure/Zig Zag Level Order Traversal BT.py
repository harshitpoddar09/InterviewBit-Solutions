# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
 
class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def zigzagLevelOrder(self, A):
        def height(A):
            if not A:
                return 0
            lheight=height(A.left)
            rheight=height(A.right)
            return max(lheight,rheight)+1
        def curLevel(A,level,flag,ans):
            if not A:
                return
            if level==1:
                ans.append(A.val)
            elif level>1:
                if flag:
                    curLevel(A.left,level-1,flag,ans)
                    curLevel(A.right,level-1,flag,ans)
                else:
                    curLevel(A.right,level-1,flag,ans)
                    curLevel(A.left,level-1,flag,ans)
            return ans
        h=height(A)
        res=[]
        flag=True
        for i in range(1,h+1):
            res.append(curLevel(A,i,flag,[]))
            flag=not flag
        return res