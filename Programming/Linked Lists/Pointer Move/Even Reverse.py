# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
 
class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def solve(self, A):
        even=ListNode(0)
        even1=even
        ans=A
        head=A
        while head and head.next:
            head=head.next
            even.next=ListNode(head.val)
            even=even.next
            head=head.next
        even2=even1.next
        even1=None
        while even2:
            new=even2.next
            even2.next=even1
            even1=even2
            even2=new
        while A and A.next:
            A=A.next
            A.val=even1.val
            A=A.next
            even1=even1.next
        return ans
