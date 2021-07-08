# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
 
class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        l=0
        a=A
        while A:
            l+=1
            A=A.next
        b=(l//2)+1-B
        if b<1:
            return -1
        c=0
        while c<b-1:
            a=a.next
            c+=1
        return a.val