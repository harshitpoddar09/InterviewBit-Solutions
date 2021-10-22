# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
 
class Solution:
    # @param A : list of linked list
    # @return the head node in the linked list
    def mergeKLists(self, A):
        nodes=[]
        for head in A:
            while head:
                nodes.append(head.val)
                head=head.next
        nodes.sort()
        cur=ListNode(nodes[0])
        ans=cur
        for i in range(1,len(nodes)):
            cur.next=ListNode(nodes[i])
            cur=cur.next
        return ans