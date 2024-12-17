class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = set()
        for index in nums:
            if index in seen:
                return True
            else:
                seen.add(index)
        return False
