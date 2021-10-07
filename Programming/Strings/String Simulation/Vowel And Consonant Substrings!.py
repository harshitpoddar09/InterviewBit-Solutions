class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        vowel=0
        cons=0
        v={'a','e','i','o','u'}
        ans=0
        for i in A:
            if i in v:
                ans+=cons
                vowel+=1
            else:
                ans+=vowel
                cons+=1
        return ans%(10**9+7)