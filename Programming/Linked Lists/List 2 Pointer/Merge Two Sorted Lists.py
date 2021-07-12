# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
 
class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def mergeTwoLists(self, A, B):
        if not A:
            return B
        if not B:
            return A
        a=[]
        while A:
            a.append(A.val)
            A=A.next
        b=[]
        while B:
            b.append(B.val)
            B=B.next
        c=sorted(a+b)
        dummy=ListNode(0)
        ans=dummy
        for i in c:
            dummy.next=ListNode(i)
            dummy=dummy.next
        return ans.next