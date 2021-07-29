from collections import Counter
class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, A, B):
        new=Counter(A)
        if B==0:
            for i in new:
                if new[i]>1:
                    return 1
            return 0
        else:
            for i in new:
                if i-B in new:
                    return 1
            return 0