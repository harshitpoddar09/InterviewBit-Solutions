# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None
 
class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def rotateRight(self, A, B):
        head=A
        length=0
        while A.next:
            A=A.next
            length+=1
        length+=1
        b=B%length
        if b==0:
            return head
        A.next=head
        idx=0
        prev=None
        while idx<length-b:
            prev=head
            head=head.next
            idx+=1
        prev.next=None
        return head