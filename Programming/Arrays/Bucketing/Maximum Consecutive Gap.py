class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, A):
        A=list(A)
        A.sort()
        ans=0
        for i in range(1,len(A)):
            cur=A[i]-A[i-1]
            ans=max(ans,cur)
        return ans