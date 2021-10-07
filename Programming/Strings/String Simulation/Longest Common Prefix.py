class Solution:
    # @param A : list of strings
    # @return a strings
    def longestCommonPrefix(self, A):
        word1=min(A)
        word2=max(A)
        count=0
        for i in range(min(len(word1),len(word2))):
            if word1[i]==word2[i]:
                count+=1
        return word1[:count]