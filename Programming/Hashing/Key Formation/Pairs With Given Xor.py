class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        s=set()
        ans=0
        for i in A:
            j=i^B
            if j in s:
                ans+=1
            s.add(i)
        return ans
