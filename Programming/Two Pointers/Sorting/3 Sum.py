class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def threeSumClosest(self, A, B):
        A.sort()
        ans=A[0]+A[1]+A[2]
        for i in range(len(A)):
            if i>0 and A[i]==A[i-1]:
                continue
            left=i+1
            right=len(A)-1
            while left<right:
                a=A[i]+A[left]+A[right]
                if a==B:
                    return a
                elif a>B:
                    if abs(a-B)<abs(ans-B):
                        ans=a
                    right-=1
                    while left<right and A[right]==A[right+1]:
                        right-=1
                else:
                    if abs(a-B)<abs(ans-B):
                        ans=a
                    left+=1
                    while left<right and A[left]==A[left-1]:
                        left+=1
        return ans