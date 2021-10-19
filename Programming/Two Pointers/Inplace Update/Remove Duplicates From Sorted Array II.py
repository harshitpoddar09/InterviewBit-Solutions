class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        i=0
        count=1
        for j in range(1,len(A)):
            if A[i]==A[j] and count<2:
                A[i+1]=A[j]
                i+=1
                count+=1
            elif A[i]!=A[j]:
                A[i+1]=A[j]
                count=1
                i+=1
        return i+1