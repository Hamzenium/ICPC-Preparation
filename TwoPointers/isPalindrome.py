class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        result = ""
        for word in s:
            if word.isalnum():
                result += word.lower()
        return result == result[::-1]

