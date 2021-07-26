class Solution:
    # @param A : tuple of list of integers
    # @return a list of integers
    def spiralOrder(self, A):
        t=0
        b=len(A)-1
        l=0
        r=len(A[0])-1
        direction=0
        ans=[]
        while t<=b and l<=r:
            if direction==0:
                for i in range(l,r+1):
                    ans.append(A[t][i])
                t+=1
                direction=1
            elif direction==1:
                for i in range(t,b+1):
                    ans.append(A[i][r])
                r-=1
                direction=2
            elif direction==2:
                for i in range(r,l-1,-1):
                    ans.append(A[b][i])
                b-=1
                direction=3
            elif direction==3:
                for i in range(b,t-1,-1):
                    ans.append(A[i][l])
                l+=1
                direction=0
        return ans
