class Solution:
    # @param A : integer
    # @return a list of integers
    def allFactors(self, A):
        if A==1:
            return [1]
        a=[]
        b=[]
        for i in range(1,int(A**0.5)+1):
            if A%i==0:
                a.append(i)
                b.insert(0,(A//i))
        a.extend(b)
        if A**0.5==int(A**0.5):
            a.remove(int(A**0.5))
        return a