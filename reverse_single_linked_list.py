# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        new_list = None
        current = head
        while current:
            next_node = current.next
            current.next = new_list
            new_list = current
            current = next_node
        return new_list


"""
here is the algorithm that the use O(N)
where we make the current Node that points to the head pointer we also use another pointer that is Null
we take the first node and point it to null, then we make the new pointer to pointer to current node, and the new poionter 
"""