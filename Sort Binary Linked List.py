# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
 
class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def solve(self, A):
        c1=0
        c0=0
        temp=A
        ans=A
        while A:
            if A.val==1:
                c1+=1
            else:
                c0+=1
            A=A.next
        while c0:
            temp.val=0
            temp=temp.next
            c0-=1
        while c1:
            temp.val=1
            temp=temp.next
            c1-=1
        return ans