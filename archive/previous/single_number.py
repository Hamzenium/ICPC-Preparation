class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = -1
        for char in nums:
            if nums.count(char) != 2:
                return char
        return result
