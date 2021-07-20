class Solution:
    # @param arrive : list of integers
    # @param depart : list of integers
    # @param K : integer
    # @return a boolean
    def hotel(self, arrive, depart, K):
        arrive.sort()
        depart.sort()
        i=0
        j=0
        while i<len(arrive) and j<len(depart):
            if arrive[i]<depart[j]:
                K-=1
                i+=1
            else:
                K+=1
                j+=1
            if K<0:
                return 0
        return 1