class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def isvalid(self,s,k,n,val):
        students = 1
        pages =0
        for i in range(n):
            pages = pages+s[i]
            if pages>val:
                students = students+1
                pages = s[i]
            if students>k:
                return 0
        return 1
        
    def books(self, A, B):
        n = len(A)
        if n==B:
            return max(A)
        if n<B:
            return -1
        if B == 1:
            return sum(A)
        start = max(A)
        end = sum(A)
        res = -1
        while start<=end:
            mid = (start+end)//2
            if self.isvalid(A,B,n,mid):
                #print(start,end,mid)
                res = mid
                end = mid-1
            else:
                start = mid+1
        return res