# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        array = []
        pointer = head
        while pointer != None:
            array += pointer.val,
            pointer = pointer.next
        return array == array[::-1]
        


        
