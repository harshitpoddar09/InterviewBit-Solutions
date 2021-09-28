class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        lo=0
        hi=len(A)-1
        while lo<=hi:
            mid=(hi+lo)//2
            if A[mid]<=B:
                lo=mid+1
            elif A[mid]>B:
                hi=mid-1
        return lo