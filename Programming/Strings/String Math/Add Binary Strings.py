class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def addBinary(self, A, B):
        ans=int(A,2)+int(B,2)
        return bin(ans)[2:]