class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        left=0
        right=0
        for i in A:
            if i=='(':
                left+=1
            else:
                if left:
                    left-=1
                else:
                    right+=1
        return left+right