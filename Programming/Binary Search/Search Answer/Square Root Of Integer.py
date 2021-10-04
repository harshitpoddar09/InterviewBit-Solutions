class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        lo=0
        hi=A
        while lo<=hi:
            mid=(lo+hi)//2
            a=mid*mid
            if a==A:
                return mid
            elif a<A:
                lo=mid+1
            else:
                hi=mid-1
        return lo-1