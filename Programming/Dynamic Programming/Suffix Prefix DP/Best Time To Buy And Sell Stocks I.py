class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        if len(A)<2:
            return 0
        cur_min=A[0]
        ans=0
        for i in range(1,len(A)):
            ans=max(ans,A[i]-cur_min)
            cur_min=min(cur_min,A[i])
        return ans
