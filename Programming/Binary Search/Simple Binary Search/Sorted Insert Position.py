class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def searchInsert(self, A, B):
        lo=0
        hi=len(A)-1
        while lo<=hi:
            mid=(hi+lo)//2
            if A[mid]==B:
                return mid
            elif A[mid]>B:
                hi=mid-1
            else:
                lo=mid+1
        return lo