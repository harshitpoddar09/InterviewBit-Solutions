class Solution:
    # @param A : string
    # @return a strings
    def reverseString(self, A):
        stack=[]
        for i in A:
            stack.append(i)
        ans=''
        while stack:
            ans+=stack[-1]
            stack.pop()
        return ans