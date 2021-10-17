class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        seen=set()
        for i in A:
            if i+B in seen:
                return 1
            elif i-B in seen:
                return 1
            else:
                seen.add(i)
        return 0
