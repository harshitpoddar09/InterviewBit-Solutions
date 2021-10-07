class Solution:
    # @param A : integer
    # @return a strings
    def countAndSay(self, n):
        ans='1'
        for i in range(n-1):
            new=''
            count=0
            current=ans[0]
            for j in ans:
                if j==current:
                    count+=1
                else:
                    new+=str(count)+current
                    count=1
                    current=j
            new+=str(count)+current
            ans=new
        return ans