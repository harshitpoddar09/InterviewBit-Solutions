class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        d={}
        for i in range(len(A)):
            cur=A[i]
            if cur in d:
                d[cur].sort()
                A[d[cur][0]]+=1
                if cur+1 in d:
                    d[cur+1].append(d[cur][0])
                else:
                    d[cur+1]=[d[cur][0]]
                d[cur].pop(0)
                d[cur].append(i)
            else:
                d[cur]=[i]
        return A
