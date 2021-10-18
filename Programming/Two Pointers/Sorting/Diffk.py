from collections import Counter
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, A, B):
        new=Counter(A)
        if B==0:
            for key in new:
                if new[key]>1:
                    return 1
            return 0
        for i in A:
            if i-B in new:
                return 1
        return 0