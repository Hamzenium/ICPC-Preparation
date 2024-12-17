class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        letters="abcdefghijklmnopqrstuvwxyz1234567890"
        word = ""
        for i in s:
            if i in letters:
                word += str(i)
        return word == word[::-1]