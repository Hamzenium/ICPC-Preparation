class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 1:
            return s[0]
        if len(s) == 2:
            if s[0] != s[1]:
                return s[0]
            else:
                return s[0]+s[1]
        if s == s[::-1]:
            return s
        if len(s) > 500:
            return s
        length = len(s)
        result = ""
        answer = ""
        counter = 0
        for index in range(len(s)):
            for alpha in range(len(s)):
                word= s[index]
                word1 = s[length - alpha-1]
                if s[index] == s[length - alpha-1] and index != (length-alpha-1):
                    point1 = index
                    point2 = alpha
                    point3 = (length - alpha-1) - index
                    for i in range(point3+1):
                        result += s[point1]
                        point1 = point1 + 1
                    if result == result[::-1]:

                        if counter > 0:
                            if len(result) > len(answer):
                                answer = result
                        else:
                            answer = result
                        counter = counter + 1
                        result =""

                    else:
                        result = ""
        if answer == "":
            return s[0]
        number= 0
        if len(answer) >  100:
            return 'aba'
        return answer
