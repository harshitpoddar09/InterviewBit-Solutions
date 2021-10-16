class Solution:
    # @param A : list of integers
    # @return an integer
    def findMinXor(self, A):
        A=sorted(A)
        ans=A[0]^A[1]
        for i in range(len(A)-1):
            ans=min(ans,A[i]^A[i+1])
        return ans