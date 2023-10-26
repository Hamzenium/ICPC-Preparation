# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        fast = head
        slow = head
        for i in range(n):
            fast = fast.next
        if not fast:
            return head.next
        
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next

        return head


 # in this algorithm we first run the first pointer till it is at nth position 
 # we again run the program till the first terminates thorugh the linked list and the slow node is eacctly behind the nth node
 # we then point the slow = slow.next.next
 # return the header
 # the time complixty of the algorithm would bee O(n), the length of the linkedlist