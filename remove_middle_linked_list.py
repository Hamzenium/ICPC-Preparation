# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        counter = 0
        pointer = head
        if not head or not head.next:
            return None
        if not head.next:
            return head
        while pointer:
            pointer = pointer.next 
            counter += 1
        if counter == 1:
            return []
        pointer = head
        index = (counter/2)
        for i in range(index-1):
            pointer = pointer.next
        pointer.next = pointer.next.next
        return head
    
# the time complexity of the algorithm takes O(n)