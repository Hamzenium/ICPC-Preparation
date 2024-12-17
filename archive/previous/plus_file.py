class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # length = len(digits) - 1
        # original_length = len(digits) - 1

        # if digits[length] < 9:
        #     digits[length] = digits[length] + 1
        # else:
        #     for index in range(len(digits)):
        #         if digits[original_length - index] == 9:
        #             digits[original_length - index] == 0
        #             if digits[original_length - (index + 1)] == 9:
        #                 digits[original_length - (index + 1)]  == 0
        #             else:
        #                 if original_length == 1:
        #                     digits.append(0)
        #                 else:
        #                     digits[original_length - (index + 1)] = digits[original_length - (index + 1)] + 1
        result =""
        array = []
        sum = 0 
        for i in digits:
            result+= str(i)
        sum = int(result)
        sum += 1
        result = str(sum)
        for i in result:
            array.append(int(i))
        return array



