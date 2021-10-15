class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        d={}
        for i in A:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for j in d:
            if d[j]==1:
                return j