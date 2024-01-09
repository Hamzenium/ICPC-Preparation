class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool"""
        length = len(nums) - 1
        for index in range(len(nums)-1,-1,-1):
            print(index)
            if index + nums[index] > length:
                length = index

        return True if length == 0 else False


sol = Solution()
nums = [3,2,1,0,4]
print(sol.canJump(nums))