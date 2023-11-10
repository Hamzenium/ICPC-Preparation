class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
        }
        sum = 0
        prev = 0
        for char in s:
            if prev < dict.get(char):
                sum += (-2 * prev) + dict.get(char)
            else:
                sum += dict.get(char)
            prev = dict.get(char)
        return sum
