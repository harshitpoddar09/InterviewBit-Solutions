class Solution:
    # @param A : list of integers
    # @return a list of integers
    def wave(self, A):
        A.sort()
        for i in range(0,len(A),2):
            if i+1<len(A):
                temp=A[i]
                A[i]=A[i+1]
                A[i+1]=temp
        return A