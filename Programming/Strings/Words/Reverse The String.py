class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        A=A.split()
        return ' '.join(A[::-1])