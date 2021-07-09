# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
 
class Solution:
    # @param A : head node of linked list
    # @return the first node in the cycle in the linked list
    def detectCycle(self, A):
        def cycle(self,A):
            tortoise=A
            hare=A
            while hare and hare.next:
                hare=hare.next.next
                tortoise=tortoise.next
                if hare==tortoise:
                    return True
            return False
        if cycle(self,A):
            b=set()
            while A:
                if b and A in b:
                    return A
                else:
                    b.add(A)
                    A=A.next
        else:
            return None