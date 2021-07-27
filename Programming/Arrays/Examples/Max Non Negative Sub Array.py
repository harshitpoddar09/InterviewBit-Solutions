class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        ans=[]
        max_sum=0
        cur_arr=[]
        cur_sum=0
        for i in A:
            if i>=0:
                cur_sum+=i
                cur_arr.append(i)
            else:
                if cur_sum>max_sum:
                    ans.clear()
                    ans.extend(cur_arr)
                    max_sum=cur_sum
                elif cur_sum==max_sum:
                    if len(cur_arr)>len(ans):
                        ans.clear()
                        ans.extend(cur_arr)
                cur_sum=0
                cur_arr.clear()
        if cur_sum>max_sum:
            ans.clear()
            ans.extend(cur_arr)
            max_sum=cur_sum
        elif cur_sum==max_sum:
            if len(cur_arr)>len(ans):
                ans.clear()
                ans.extend(cur_arr)
        return ans