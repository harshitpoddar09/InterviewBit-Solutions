from collections import Counter
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def dNums(self, A, B):
        d=Counter(A[:B])
        distinct=0
        for key in d:
            distinct+=1
        ans=[distinct]
        for i in range(B,len(A)):
            if d[A[i-B]]==1:
                distinct-=1
            d[A[i-B]]-=1
            if d[A[i-B]]==0:
                del d[A[i-B]]
            if A[i] not in d:
                distinct+=1
                d[A[i]]=0
            d[A[i]]+=1
            ans.append(distinct)
        return ans
