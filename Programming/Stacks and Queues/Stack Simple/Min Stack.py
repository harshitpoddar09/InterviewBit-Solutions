class MinStack:
    # @param x, an integer
    def __init__(self):
        self.stack=[]
        self.min_stack=[]
        
    def push(self, x):
        self.stack.append(x)
        if len(self.min_stack)==0 or self.min_stack[-1]>=x:
            self.min_stack.append(x)
 
    # @return nothing
    def pop(self):
        if self.stack:
            if self.stack[-1]==self.min_stack[-1]:
                self.min_stack.pop()
            self.stack.pop()
 
    # @return an integer
    def top(self):
        if not self.stack:
            return -1
        return self.stack[-1]
 
    # @return an integer
    def getMin(self):
        if not self.stack:
            return -1
        return self.min_stack[-1]