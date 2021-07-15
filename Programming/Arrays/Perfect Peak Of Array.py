class Solution:
    # @param A : list of integers
    # @return an integer
    def perfectPeak(self, A):
        cur_max=A[0]
        for i in range(1,len(A)-1):
            cur_max=max(cur_max,A[i-1])
            if A[i]>cur_max and A[i]<min(A[i+1:]):
                return 1
        return 0