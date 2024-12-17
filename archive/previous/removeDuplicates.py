class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        pointer = 0
        for i in range(1,len(nums)):
            if nums[i] != nums[pointer]:
                pointer = pointer + 1
                nums[pointer] = nums[i]
        return pointer + 1
