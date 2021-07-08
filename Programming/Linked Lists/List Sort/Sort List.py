# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
 
class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def sortList(self, A):
        a=[]
        while A:
            a.append(A.val)
            A=A.next
        a.sort()
        dummy=ListNode(0)
        ans=dummy
        for i in a:
            dummy.next=ListNode(i)
            dummy=dummy.next
        return ans.next