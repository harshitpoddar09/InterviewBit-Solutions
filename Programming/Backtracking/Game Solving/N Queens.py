class Solution:
    # @param A : integer
    # @return a list of list of strings
    def solveNQueens(self, A):
        def isSafe(chess,row,col):
            for i in range(row-1,-1,-1):
                if chess[i][col]==1:
                    return False
            p=row-1
            q=col-1
            while p>=0 and q>=0:
                if chess[p][q]==1:
                    return False
                p-=1
                q-=1
            p=row-1
            q=col+1
            while p>=0 and q<len(chess):
                if chess[p][q]==1:
                    return False
                p-=1
                q+=1
            return True
        def Nqueens(chess,qsf,row,idx):
            if row==len(chess):
                idx.append(qsf)
                return 
            for col in range(len(chess)):
                if isSafe(chess,row,col):
                    chess[row][col]=1
                    Nqueens(chess,qsf+[[row,col]],row+1,idx)
                    chess[row][col]=0
        chess=[[0 for i in range(A)] for j in range(A)]
        idx=[]
        Nqueens(chess,[],0,idx)
        ans=[]
        for i in idx:
            ans.append(['' for j in range(A)])
            cur=0
            for k in i:
                q=k[1]
                ptr=0
                while ptr<A:
                    if ptr==q:
                        ans[-1][cur]+='Q'
                    else:
                        ans[-1][cur]+='.'
                    ptr+=1
                cur+=1
        return ans
