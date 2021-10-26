class Solution:
    # @param A : integer
    # @return an integer
    def climbStairs(self, A):
        results={}
        def getPaths(n):
            if n==0:
                return 1
            elif n<0:
                return 0
            if n-1 in results:
                path1=results[n-1]
            else:
                path1=getPaths(n-1)
                results[n-1]=path1
            if n-2 in results:
                path2=results[n-2]
            else:
                path2=getPaths(n-2)
                results[n-2]=path2
            return path1+path2
        return getPaths(A)
