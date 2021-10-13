class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLastWord(self, A):
        len_prev=0
        len_cur=0
        for i in A:
            if i==' ':
                if len_cur==0:
                    len_prev=max(0,len_prev)
                else:
                    len_prev=len_cur
                len_cur=0
            else:
                len_cur+=1
        if len_cur==0:
            return len_prev
        else:
            return len_cur
