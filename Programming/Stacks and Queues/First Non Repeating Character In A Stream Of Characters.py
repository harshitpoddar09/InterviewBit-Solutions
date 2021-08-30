class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        ans=''
        seen={}
        queue=[]
        for i in A:
            if i not in seen:
                seen[i]=0
            seen[i]+=1
            queue.append(i)
            while queue and seen[queue[0]]>1:
                queue.pop(0)
            if queue:
                ans+=queue[0]
            else:
                ans+='#'
        return ans