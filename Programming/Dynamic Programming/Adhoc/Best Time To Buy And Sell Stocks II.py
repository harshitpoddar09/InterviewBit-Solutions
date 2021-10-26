class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        profit=[max(0,A[i+1]-A[i]) for i in range(len(A)-1)]
        return sum(profit) 
