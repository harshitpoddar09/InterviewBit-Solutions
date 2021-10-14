class Solution:
    # @param A : unsigned integer
    # @return an unsigned integer
    def reverse(self, A):
        A=bin(A)[2:]
        A=(32-len(A))*'0'+A
        return int(A[::-1],2)