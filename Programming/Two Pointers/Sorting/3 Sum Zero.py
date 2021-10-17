class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def threeSum(self, A):
        A.sort()
        ans=[]
        for i in range(len(A)):
            if i>0 and A[i]==A[i-1]:
                continue
            left=i+1
            right=len(A)-1
            while left<right:
                cur_sum=A[i]+A[left]+A[right]
                if cur_sum>0:
                    right-=1
                elif cur_sum<0:
                    left+=1
                else:
                    ans.append([A[i],A[left],A[right]])
                    left+=1
                    right-=1
                    while left<right and A[left]==A[left-1]:
                        left+=1
                    while left<right and A[right]==A[right+1]:
                        right-=1
        return ans