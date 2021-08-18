class Solution:
    # @param A : string
    # @return a list of strings
    def letterCombinations(self, A):
        d={'0':'0','1':'1','2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        if len(A)==0:
            return []
        def letter(A):
            if len(A)==0:
                return ['']
            char=A[0]
            rem_A=A[1:]
            rres=letter(rem_A)
            mres=[]
            for i in d[char]:
                for j in rres:
                    mres.append(i+j)
            return mres
        return letter(A)
