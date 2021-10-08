class Solution:
    # @param A : string
    # @return an integer
    def romanToInt(self, A):
        roman_1=['CM','CD','XC','XL','IX','IV']
        roman_2=['M','D','C','L','X','V','I']
        integer_1=[900,400,90,40,9,4]
        integer_2=[1000,500,100,50,10,5,1]
        ans=0
        for i in range(6):
            if roman_1[i] in A:
                ans+=integer_1[i]
                A=A.replace(roman_1[i],'')
        for j in A:
            ans+=integer_2[roman_2.index(j)]
            A=A.replace(j,'',1)
        return ans
