# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
 
class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def removeNthFromEnd(self, A, B):
        l=0
        a=A
        while A:
            l+=1
            A=A.next
        if B>=l:
            return a.next
        ans=a
        c=0
        prev=None
        while c<l-B:
            prev=a
            a=a.next
            c+=1
        prev.next=a.next
        return ans