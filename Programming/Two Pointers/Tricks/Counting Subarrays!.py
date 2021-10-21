class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        ans=0
        w_start=0
        w_end=0
        cur=0
        while w_end<len(A):
            cur+=A[w_end]
            while cur>=B:
                cur-=A[w_start]
                w_start+=1
            ans+=w_end-w_start+1
            w_end+=1
        return ans