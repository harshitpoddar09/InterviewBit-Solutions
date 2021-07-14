class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        for i in range(len(A)):
            A[i]=str(A[i])
        num=''.join(A)
        num=int(num)+1
        num=str(num)
        return list(num)