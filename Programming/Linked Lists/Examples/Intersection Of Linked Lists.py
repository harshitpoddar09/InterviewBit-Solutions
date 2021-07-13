# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
 
class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def getIntersectionNode(self, A, B):
        a=A
        l1=0
        while A:
            l1+=1
            A=A.next
        b=B
        l2=0
        while B:
            l2+=1
            B=B.next
        if l1>l2:
            while l1>l2:
                a=a.next
                l1-=1
            while b:
                if a==b:
                    return a
                else:
                    a=a.next
                    b=b.next
        else:
            while l1<l2:
                b=b.next
                l2-=1
            while b:
                if a==b:
                    return a
                else:
                    a=a.next
                    b=b.next
        return None 