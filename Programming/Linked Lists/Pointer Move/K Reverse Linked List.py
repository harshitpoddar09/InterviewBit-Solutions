# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None
 
class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def reverseList(self, head, k):
        if k==1:
            return head
        prev=None
        while head:
            count=0
            b=head
            if prev==None:
                while head and count<k:
                    new=head.next
                    head.next=prev
                    prev=head
                    head=new
                    count+=1
                    ans=prev
            else:
                while head and count<k:
                    new=head.next
                    head.next=prev
                    prev=head
                    head=new
                    count+=1
                tail.next=prev
            tail=b
        tail.next=None
        return ans