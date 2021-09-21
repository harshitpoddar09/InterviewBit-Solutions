class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def rotate(self, A):
        n=len(A[0])
        for i in range(n//2):
            for j in range(i,n-i-1):
                temp=A[i][j]
                A[i][j]=A[n-1-j][i]
                A[n-1-j][i]=A[n-1-i][n-1-j]
                A[n-1-i][n-1-j]=A[j][n-1-i]
                A[j][n-1-i]=temp
        return A