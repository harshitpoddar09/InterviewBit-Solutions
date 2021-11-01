from collections import Counter
import math
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def majorityElement(self, A):
        d=Counter(A)
        for key in d:
            if d[key]>math.floor(len(A)/2):
                return key