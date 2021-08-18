class Solution:
    # @param A : tuple of strings
    # @return a list of list of integers
    def anagrams(self, A):
        new=[''.join(sorted(i)) for i in A]
        d={}
        for i in range(len(A)):
            if new[i] not in d:
                d[new[i]]=[]
            d[new[i]].append(i+1)
        ans=[]
        for key in d:
            ans.append(d[key])
        return ans