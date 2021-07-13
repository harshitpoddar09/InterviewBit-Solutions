class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def coverPoints(self, A, B):
        ans=0
        for i in range(1,len(A)):
            d=min(abs(A[i]-A[i-1]),abs(B[i]-B[i-1]))
            ans+=abs(A[i]-A[i-1])+abs(B[i]-B[i-1])-d
        return ans
