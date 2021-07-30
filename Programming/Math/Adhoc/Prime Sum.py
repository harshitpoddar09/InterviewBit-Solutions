class Solution:
    # @param A : integer
    # @return a list of integers
    def primesum(self, A):
        def isprime(n):
            if n<2:
                return False
            if n==2 or n==3:
                return True
            if n%2==0:
                return False
            for i in range(3,int(n**0.5)+1,2):
                if n%i==0:
                    return False
            return True
        ans=[2,2]
        if A==4:
            return ans
        i=3
        while i<A//2 + 1:
            if isprime(i):
                if isprime(A-i):
                    ans=[i,A-i]
                    return ans
            i+=2