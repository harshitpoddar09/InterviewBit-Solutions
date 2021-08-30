class Solution:
    # @param A : list of strings
    # @return an integer
    def evalRPN(self, A):
        stack=[]
        operations={'+','-','*','/'}
        for i in A:
            if i in operations:
                if i=='+':
                    a=stack[-2]+stack[-1]
                    stack.pop()
                    stack.pop()
                    stack.append(a)
                elif i=='-':
                    a=stack[-2]-stack[-1]
                    stack.pop()
                    stack.pop()
                    stack.append(a)
                elif i=='*':
                    a=stack[-2]*stack[-1]
                    stack.pop()
                    stack.pop()
                    stack.append(a)
                else:
                    a=stack[-2]//stack[-1]
                    stack.pop()
                    stack.pop()
                    stack.append(a)
            else:
                stack.append(int(i))
        return stack[0]