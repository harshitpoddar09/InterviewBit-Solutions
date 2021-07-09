# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
 
class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def addTwoNumbers(self, A, B):
        l1=0
        a=A
        while A:
            l1+=1
            A=A.next
        l2=0
        b=B
        while B:
            l2+=1
            B=B.next
        def add(self,p,q):         #len(p)>len(q)
            carry=0
            ans=p
            prev=None
            while q:
                s=p.val+q.val+carry
                if s>9:
                    carry=1
                else:
                    carry=0
                p.val=s%10
                prev=p
                p=p.next
                q=q.next
            while p:
                s=p.val+carry
                if s==10:
                    carry=1
                else:
                    carry=0
                p.val=s%10
                prev=p
                p=p.next
            if carry==1:
                prev.next=ListNode(1)
            return ans
        if l1>l2:
            return add(self,a,b)
        else:
            return add(self,b,a)