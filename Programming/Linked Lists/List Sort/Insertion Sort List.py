# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None
 
class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def insertionSortList(self, head):
        if not head or not head.next:
            return head
        
        dummy = ListNode(float('-inf'))
        dummy.next = head
        end = head
        runner = end.next
        
        while runner:
            if runner.val >= end.val:
                end, runner = runner, runner.next
            else:
                put = dummy
                while put.next.val < runner.val:
                    put = put.next
                # find the location to insert node
                
                end.next = runner.next
                runner.next = put.next
                put.next = runner
                # insert
                
                runner = end.next
                # update runner
        
        return dummy.next