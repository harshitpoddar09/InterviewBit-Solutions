class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        d={}
        for i in A:
            if i in d:
                return i
            else:
                d[i]=1
        return -1