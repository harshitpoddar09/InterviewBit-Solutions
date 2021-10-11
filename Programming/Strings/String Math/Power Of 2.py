class Solution:
    # @param A : string
    # @return an integer
    def power(self, A):
        A=int(A)
        if A==0 or A==1:
            return 0
        if A&(A-1)==0:
            return 1
        return 0