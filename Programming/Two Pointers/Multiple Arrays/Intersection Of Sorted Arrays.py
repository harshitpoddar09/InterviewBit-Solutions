class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a list of integers
    def intersect(self, A, B):
        i=0
        j=0
        ans=[]
        while i<len(A) and j<len(B):
            if A[i]==B[j]:
                ans.append(A[i])
                i+=1
                j+=1
            elif A[i]>B[j]:
                j+=1
            else:
                i+=1
        return ans