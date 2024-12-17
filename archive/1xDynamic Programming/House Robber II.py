class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def helper(nums):
            rob1, rob2 = 0 , 0
            for n in range(len(nums)):
                temp = max(rob1 + nums[n], rob2)
                rob1 = rob2
                rob2 = temp
            return rob2
        return max(nums[0],helper(nums[1:0]),helper(nums[:-1]))

        


algorithm = Solution()
nums = [1,2,3,1]
print(algorithm.rob(nums))