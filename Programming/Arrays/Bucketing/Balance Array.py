class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        ans=0
        pre_o=0
        pre_e=0
        post_o=0
        post_e=0
        for j in range(1,len(A),2):
            post_e+=A[j]
            if j+1<len(A):
                post_o+=A[j+1]
        for i in range(len(A)):
            if i%2==0:
                if pre_o+post_o==pre_e+post_e:
                    ans+=1
                pre_e+=A[i]
                if i+1<len(A):
                    post_e-=A[i+1]
            else:
                if pre_o+post_o==pre_e+post_e:
                    ans+=1
                pre_o+=A[i]
                if i+1<len(A):
                    post_o-=A[i+1]
        return ans