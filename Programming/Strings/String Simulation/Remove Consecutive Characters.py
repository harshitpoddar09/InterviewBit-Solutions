class Solution:
    # @param A : string
    # @param B : integer
    # @return a strings
    def solve(self, A, B):
        a=set(A)
        for i in a:
            if i*B in A and i*(B+1) not in A:
                A=A.replace(i*B,'')
        return A