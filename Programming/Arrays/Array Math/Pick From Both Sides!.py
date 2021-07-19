class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        cur_sum=sum(A[:B])
        ans=cur_sum
        j=len(A)-1
        for i in range(B-1,-1,-1):
            cur_sum-=A[i]
            cur_sum+=A[j]
            j-=1
            ans=max(cur_sum,ans)
        return ans