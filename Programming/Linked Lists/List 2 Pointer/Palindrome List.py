# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
 
class Solution:
    # @param A : head node of linked list
    # @return an integer
    def lPalin(self, A):
        length=0
        second=A
        first=A
        while A:
            length+=1
            A=A.next
        if length==1:
            return 1
        idx=0
        if length%2==0:           
            while idx<length//2:
                second=second.next
                idx+=1
        else:
            while idx<(length//2)+1:
                second=second.next
                idx+=1
        new=second
        prev=None
        while second.next:
            new=second
            second=second.next
            new.next=prev
            prev=new
        second.next=prev
        while second:
            if first.val!=second.val:
                return 0
            else:
                first=first.next
                second=second.next
        return 1
