class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        elif n ==1:
            return True
        else:
            while n % 3 == 0:
                n = n / 3
                if n == 1:
                    return True
            return False
