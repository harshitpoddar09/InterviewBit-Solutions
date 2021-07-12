# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
 
class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, A):
        if not A:
            return A
        ans=A
        while A.next:
            if A.val==A.next.val:
                A.next=A.next.next
            else:
                A=A.next
        return ans