class Solution:
    # @param A : string
    # @return an integer
    def titleToNumber(self, A):
        ans=0
        n=len(A)
        for i,j in enumerate(A):
            ans+=(ord(j)-64)*(26**(n-i-1))
        return ans