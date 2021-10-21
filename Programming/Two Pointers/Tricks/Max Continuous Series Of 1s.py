class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def maxone(self, A, B):
        count1=0
        w_start=0
        max_len=0
        for w_end in range(len(A)):
            if A[w_end]==1:
                count1+=1
            if w_end-w_start+1-count1>B:
                if A[w_start]==1:
                    count1-=1
                w_start+=1
            if w_end-w_start+1>max_len:
                max_len=w_end-w_start+1
                a=w_start
                b=w_end
        ans=[i for i in range(a,b+1)]
        return ans