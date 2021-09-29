class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def searchRange(self, A, B):
        lo=0
        hi=len(A)-1
        idx=-1
        while lo<=hi:
            mid=(lo+hi)//2
            if A[mid]==B:
                idx=mid
                break
            elif A[mid]>B:
                hi=mid-1
            else:
                lo=mid+1
        if idx==-1:
            return [-1,-1]
        i=idx
        j=idx
        while i>-1 and A[i]==B:
            i-=1
        while j<len(A) and A[j]==B:
            j+=1
        return [i+1,j-1]