class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        if max(A)<0:
            return max(A)
        ans=0
        cur_sum=0
        for i in A:
            cur_sum+=i
            cur_sum=max(cur_sum,0)
            ans=max(cur_sum,ans)
        return ans