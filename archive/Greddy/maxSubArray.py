class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = nums[0]
        total = 0
        for num in nums:
            total += num
            res = max(total,res)
            if total < 0:
                total = 0
        return res

sol = Solution()
nums = [-2,1]
print(sol.maxSubArray(nums))