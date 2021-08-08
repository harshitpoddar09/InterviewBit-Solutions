class Solution:
    # @param A : integer
    # @return a list of integers
    def sieve(self, A):
        arr=[1 for i in range(A+1)]
        arr[0]=0
        arr[1]=0
        p=2
        while p*p<A+1:
            if arr[p]==1:
                for i in range(p*p,A+1,p):
                    arr[i]=0
            p+=1
        ans=[i for i in range(2,A+1) if arr[i]==1]
        return ans