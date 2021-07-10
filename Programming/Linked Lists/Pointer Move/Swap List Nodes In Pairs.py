# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
 
class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def swapPairs(self, A):
        if not A or not A.next:
            return A
        cur=A.next
        A.next=cur.next
        cur.next=A
        ans=cur
        prev=A
        A=prev.next
        while A and A.next:
            cur=A.next
            A.next=cur.next
            cur.next=A
            prev.next=cur
            prev=A
            A=prev.next
        return ans