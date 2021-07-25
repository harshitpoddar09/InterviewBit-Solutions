class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def setZeroes(self, A):
        idx_c=set()
        for i in range(len(A)):
            idx_r=set()
            for j in range(len(A[0])):
                if A[i][j]==0:
                    idx_r.add(i)
                    idx_c.add(j)
            if idx_r:
                A[i]=[0 for k in range(len(A[0]))]
        for p in idx_c:
            for q in range(len(A)):
                A[q][p]=0
        return A
