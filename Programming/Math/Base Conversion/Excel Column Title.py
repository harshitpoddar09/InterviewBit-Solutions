class Solution:
    # @param A : integer
    # @return a strings
    def convertToTitle(self, A):
        ans=''
        while A:
            A=A-1
            i=A%26
            ans=chr(i+65)+ans
            A=A//26
        return ans