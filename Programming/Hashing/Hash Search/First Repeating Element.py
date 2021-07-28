from collections import Counter
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        new=Counter(A)
        for i in A:
            if new[i]>1:
                return i
        return -1
