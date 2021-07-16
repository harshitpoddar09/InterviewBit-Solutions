class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        l=0
        r=len(A)-1
        ans=[]
        while l<=r:
            if abs(A[l])>abs(A[r]):
                ans.append(A[l]**2)
                l+=1
            else:
                ans.append(A[r]**2)
                r-=1
        return ans[::-1]