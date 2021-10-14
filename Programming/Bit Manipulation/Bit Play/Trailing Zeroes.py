class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        A=bin(A)[2:][::-1]
        ans=0
        i=0
        while A[i]=='0':
            ans+=1
            i+=1
        return ans