from collections import Counter
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        b=Counter(A)
        b=b.items()
        for key,value in b:
            if value>len(A)/3:
                return key
        return -1