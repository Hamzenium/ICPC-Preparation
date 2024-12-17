class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        array = list(s)
        length = len(array)
        answer = []
        for i in range(len(array)):
            pointer = (length-1) - i
            s[i] = array[pointer]
        return answer
