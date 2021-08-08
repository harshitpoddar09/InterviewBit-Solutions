class Solution:
    # @param A : integer
    # @return an integer
    def isPrime(self, A):
        if A<2:
            return 0
        elif A==2 or A==3:
            return 1
        if A%2==0:
            return 0
        for i in range(3,int(A**0.5)+1):
            if A%i==0:
                return 0
        return 1
