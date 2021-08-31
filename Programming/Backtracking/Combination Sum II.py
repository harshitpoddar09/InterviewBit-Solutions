res = {}
def backtrack(A,subset,index,target,currsum):
   if currsum==target:
       temp = list(subset)
       res.append(temp)
       return 
   for i in range(index,len(A)):
       if i>index and A[i]==A[i-1]:
           continue
       elif A[i]+currsum<=target:
           subset.append(A[i])
           backtrack(A,subset,i+1,target,currsum+A[i])
           subset.pop()
       else:
           return
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def combinationSum(self, A, B):
        global res
        res = []
        A.sort()
        backtrack(A,[],0,B,0)
        return res