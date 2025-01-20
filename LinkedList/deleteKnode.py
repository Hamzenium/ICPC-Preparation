
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        newNode = ListNode(0,head)
        left = newNode
        right = head

        while n > 0:
            right = right.next
            n = n - 1

        while right:
            right = right.next
            left=left.next

        left.next = left.next.next
        return newNode.next
