class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        if max(A)<=0:
            return 1
        A=[i for i in A if i>0]
        A=set(A)
        for i in range(1,max(A)):
            if i not in A:
                return i
        return max(A)+1