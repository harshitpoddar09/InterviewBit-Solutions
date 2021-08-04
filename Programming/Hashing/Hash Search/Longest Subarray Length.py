from collections import Counter
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        d={}
        cur_sum=0
        ans=0
        for i in range(len(A)):
            if A[i]==1:
                cur_sum+=1
            else:
                cur_sum-=1
            if cur_sum==1:
                ans=max(ans,i+1)
            else:
                if cur_sum not in d:
                    d[cur_sum]=i
                if cur_sum-1 in d:
                    ans=max(ans,i-d[cur_sum-1])
        return ans