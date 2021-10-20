class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def removeElement(self, A, B):
        non_b=0
        i=0
        while i<len(A):
            if A[i]!=B:
                A[non_b]=A[i]
                non_b+=1
            i+=1
        return non_b