class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        start=[]
        stop=[]
        for i in A:
            start.append(i[0])
            stop.append(i[1])
        start.sort()
        stop.sort()
        i,j=0,0
        cur=0
        ans=0
        while i<len(start) and j<len(stop):
            if start[i]<stop[j]:
                cur+=1
                i+=1
            else:
                cur-=1
                j+=1
            ans=max(ans,cur)
        return ans
