import math
class Solution:
    # @param A : integer
    # @return an integer
    def isPower(self, A):
        sol=0
        if A==1:
            return 1
        for i in range(2,int(A**0.5)+1):
            sol=math.log(A,i)
            sol=round(sol,5)
            if sol==int(sol):
                return 1
        return 0