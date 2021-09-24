# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
 
class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.stack=[]
        while root:
            self.stack.append(root)
            root=root.left
 
    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return self.stack
 
    # @return an integer, the next smallest number
    def next(self):
        cur=self.stack.pop()
        node=cur.right
        while node:
            self.stack.append(node)
            node=node.left
        return cur.val
 
# Your BSTIterator will be called like this:
# i = BSTIterator(root)
# while i.hasNext(): print i.next(),