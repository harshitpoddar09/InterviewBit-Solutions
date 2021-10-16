class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        ans=0
        for i in range(len(A)):
            freq=(i+1)*(len(A)-i)
            if freq%2==1:
                ans=ans^A[i]
        return ans