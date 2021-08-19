class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        stack=[]
        for i in A:
            if i=='(':
                stack.append(')')
            else:
                if stack and i==stack[0]:
                    stack.pop(0)
                else:
                    return 0
        if stack:
            return 0
        else:
            return 1
