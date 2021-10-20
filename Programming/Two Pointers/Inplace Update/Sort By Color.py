class Solution:
    # @param A : list of integers
    # @return A after the sort
    def sortColors(self, A):
        c0=0
        c1=0
        c2=0
        for i in A:
            if i==0:
                c0+=1
            elif i==1:
                c1+=1
            else:
                c2+=1
        j=0
        while j<len(A) and c0:
            A[j]=0
            c0-=1
            j+=1
        while j<len(A) and c1:
            A[j]=1
            c1-=1
            j+=1
        while j<len(A) and c2:
            A[j]=2
            c1-=1
            j+=1
        return A