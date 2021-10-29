class Solution:
    # @param A : list of integers
    # @return an integer
    def canJump(self, A):
        last=len(A)-1
        for i in range(len(A)-2,-1,-1):
            if i+A[i]>=last:
                last=i
        if last==0:
            return 1
        return 0