class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def searchMatrix(self, A, B):
        if len(A)==0:
            return 0
        n=len(A)
        m=len(A[0])
        left=0
        right=n*m-1
        while(left<=right):
            mid=(left+right)//2
            i=mid//m
            j=mid%m
            if(A[i][j]==B):
                return 1
            elif(A[i][j]<B):
                left=mid+1
            else:
                right=mid-1
        return 0