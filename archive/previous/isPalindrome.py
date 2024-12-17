class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        s = [char.lower() for char in s if char.isalnum()]
        return s == s[::-1]
    

    #time comopleixty of the algorithm will be 0(n), since all step
"""
Iterating over the characters in the string s and applying char.lower() and char.isalnum() operations takes O(N) time complexity, where N is the length of the original string s.

Creating a list comprehension based on the filtered characters also takes O(N) time complexity because each character is processed once.

Reversing a list using slicing (s[::-1]) takes O(N) time complexity because it needs to create a reversed copy of the list.

Finally, comparing two lists for equality (s == s[::-1]) takes O(N) time complexity because it requires comparing each element in the list."""