class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A=sorted(A)
        n=len(A)
        for i in range(n):
            j=i+1
            while j<n and A[j]==A[i]:
                j+=1
            if A[i]==n-j:
                return 1
        return -1
