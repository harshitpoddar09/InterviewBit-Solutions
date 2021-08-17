class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def permute(self, A):
        final=[]
        def perm(A,ans,final):
            if len(A)==0:
                final.append(ans)
                return
            for i in range(len(A)):
                digit=A[i]
                rA=A[:i]+A[i+1:]
                perm(rA,ans+[digit],final)
        perm(A,[],final)
        return final