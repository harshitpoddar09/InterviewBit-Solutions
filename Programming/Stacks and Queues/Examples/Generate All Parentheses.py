class Solution:
    # @param A : string
    # @return an integer
    def isValid(self, A):
        stack=[]
        for i in A:
            if i=='{':
                stack.append('}')
            elif i=='[':
                stack.append(']')
            elif i=='(':
                stack.append(')')
            elif i=='}':
                if stack and stack[-1]==i:
                    stack.pop()
                else:
                    return 0
            elif i=='[':
                if stack and stack[-1]==i:
                    stack.pop()
                else:
                    return 0
            else:
                if stack and stack[-1]==i:
                    stack.pop()
                else:
                    return 0
        if len(stack)==0:
            return 1
        return 0