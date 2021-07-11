# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None
 
class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, A):
        if not A:
            return A
        prev=None
        a=set()
        ans=A
        while A and A.next:
            if A.val==A.next.val:
                a.add(A.val)
                while A and A.val in a:
                    A=A.next
                if prev==None:
                    ans=A
                else:
                    prev.next=A
                a.clear()
            else:
                prev=A
                A=A.next
        return ans