# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
 
class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @param C : integer
    # @return the head node in the linked list
    def reverseBetween(self, A, B, C):
        if B==C:
            return A
        prev=None
        count=1
        ans=A
        while count<B:
            count+=1
            prev=A
            A=A.next
        a1=A
        temp=None
        while count<=C:
            count+=1
            new=A.next
            A.next=temp
            temp=A
            A=new
        a1.next=A
        if B!=1:
            prev.next=temp
            return ans
        else:
            return temp