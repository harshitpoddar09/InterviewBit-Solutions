from collections import Counter
class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        d={}
        for i in range(1,len(A)+1):
            d[i]=0
        for j in A:
            d[j]+=1
        a=0
        b=0
        for k in range(1,len(A)+1):
            if d[k]==2:
                a=k
            elif d[k]==0:
                b=k
        return [a,b]