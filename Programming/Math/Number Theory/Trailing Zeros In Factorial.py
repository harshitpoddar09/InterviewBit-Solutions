class Solution:
    # @param A : integer
    # @return an integer
    def trailingZeroes(self, n):
        ans=0
        for i in range(5,n+1,5):
            cur=i
            while cur%5==0:
                ans+=1
                cur//= 5
        return ans