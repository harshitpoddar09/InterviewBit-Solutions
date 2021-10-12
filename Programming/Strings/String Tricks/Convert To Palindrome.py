class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        left=0
        right=len(A)-1
        if A==A[::-1] and len(A)%2==1:
            return 1
        while A[left]==A[right] and left<=right:
            left+=1
            right-=1
        a=A[:left]+A[left+1:]
        b=A[:right]+A[right+1:]
        if a==a[::-1] or b==b[::-1]:
            return 1
        return 0
