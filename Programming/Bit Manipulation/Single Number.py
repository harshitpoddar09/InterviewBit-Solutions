class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        ans=0
        for i in A:
            ans=ans^i
        return ans