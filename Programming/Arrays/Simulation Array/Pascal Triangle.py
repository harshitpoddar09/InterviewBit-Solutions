class Solution:
    # @param A : integer
    # @return a list of list of integers
    def solve(self, A):
        if A==0:
            return []
        if A==1:
            ans=[[1]]
        elif A>=2:
            ans=[[1],[1,1]]
        for i in range(2,A):
            row=[1]
            j=0
            while j<len(ans[i-1])-1:
                row.append(ans[i-1][j]+ans[i-1][j+1])
                j+=1
            row.append(1)
            ans.append(row)
        return ans