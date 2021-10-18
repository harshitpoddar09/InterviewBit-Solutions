class Solution:
    # @param A : list of integers
    # @return an integer
    def nTriang(self, A):
        A.sort()
        ans=0
        for i in range(len(A)-1,1,-1):
            left=0
            right=i-1
            while left<right:
                if A[left]+A[right]>A[i]:
                    ans+=right-left
                    right-=1
                else:
                    left+=1
        return ans%(10**9+7)