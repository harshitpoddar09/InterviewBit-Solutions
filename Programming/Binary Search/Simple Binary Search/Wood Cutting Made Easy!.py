class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        def cutwood(height):
            sum=0
            for i in A:
                if i>height:
                    sum+=i-height
            return sum>=B
        lo=0
        hi=max(A)
        while lo<=hi:
            mid=(lo+hi)//2
            if cutwood(mid):
                lo=mid+1
            else:
                hi=mid-1
        return lo-1