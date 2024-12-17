class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        boolean = False
        if x < 0:
            x = x * -1
            boolean = True
        word = str(x)
        answer = word[::-1]
        if boolean == True:
            answer = ''.join(('-',answer))
        if int(answer) > -2147483648 and int(answer) < 2147483647:
            return int(answer)
        else:
            return 0
