from collections import OrderedDict
class Solution:
    # @param A : list of integers
    # @return an integer
    def bulbs(self, A):
        d=OrderedDict()
        for i in range(len(A)):
            d[i]=A[i]
        ans=0
        flip=0
        for key in d:
            if d[key]==1:
                if flip%2==0:
                    continue
                else:
                    flip+=1
                    ans+=1
            else:
                if flip%2==1:
                    continue
                else:
                    flip+=1
                    ans+=1
        return ans