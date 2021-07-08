# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
 
class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def partition(self, A, B):
        less=ListNode(0)
        less1=less
        more=ListNode(0)
        more1=more
        while A:
            if A.val<B:
                less.next=ListNode(A.val)
                less=less.next
            else:
                more.next=ListNode(A.val)
                more=more.next
            A=A.next
        more.next=None
        less.next=more1.next
        return less1.next