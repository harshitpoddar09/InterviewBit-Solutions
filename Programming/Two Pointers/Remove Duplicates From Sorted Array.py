class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        non_duplicate=0
        i=1
        while i<len(A):
            if A[non_duplicate]!=A[i]:
                A[non_duplicate+1]=A[i]
                non_duplicate+=1
            i+=1
        return non_duplicate+1