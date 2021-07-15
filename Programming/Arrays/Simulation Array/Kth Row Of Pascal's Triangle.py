class Solution:
    # @param A : integer
    # @return a list of integers
    def getRow(self, A):
        if A==0:
            return [1]
        elif A==1:
            return [1,1]
        old=[1,1]
        for i in range(1,A):
            ans=[1]
            j=0
            while j<len(old)-1:
                ans.append(old[j]+old[j+1])
                j+=1
            ans.append(1)
            old=ans
        return ans