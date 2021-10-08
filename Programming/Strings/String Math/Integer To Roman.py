class Solution:
    # @param A : integer
    # @return a strings
    def intToRoman(self, A):
        roman=['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        integer=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
        ans=""
        for i in range(len(integer)):
            ans+=roman[i]*(A//integer[i])
            A=A%integer[i]
        return ans