class Solution:
    # @param A : integer
    # @return an integer
    def reverse(self, A):
        A=str(A)
        ans=0
        if A[0]=='-':
            ans=int('-'+A[1:][::-1])
        else:
            ans=int(A[::-1])
        limitp=2**32
        limitn=2**31
        if ans<=limitp and ans>=-limitn:
            return ans
        else:
            return 0