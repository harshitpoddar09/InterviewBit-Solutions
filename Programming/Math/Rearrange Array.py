class Solution:
    # @param A : list of integers
    # Modify the array A which is passed by reference. 
    # You do not need to return anything in this case. 
    def arrange(self, A):
        ans=[]
        for i in range(len(A)):
            A.append(A[A[i]])
        for i in range(len(A)//2):
            A.pop(0)
        return A