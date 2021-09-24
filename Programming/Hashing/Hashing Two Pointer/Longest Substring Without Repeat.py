class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLongestSubstring(self, A):
        queue=[]
        ans=0
        for i in A:
            while i in queue:
                queue.pop(0)
            else:
                queue.append(i)
            ans=max(ans,len(queue))
        return ans
