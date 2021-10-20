class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        max_ones=0
        max_length=0
        w_start=0
        for w_end in range(len(A)):
            if A[w_end]==1:
                max_ones+=1
            if w_end-w_start+1-max_ones>B:
                if A[w_start]==1:
                    max_ones-=1
                w_start+=1
            max_length=max(max_length,w_end-w_start+1)
        return max_length