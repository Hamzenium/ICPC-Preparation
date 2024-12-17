class Solution(object):
    def rob(self, nums):
        if len(nums) < 2:
            return max(nums)

        dp = [0] * (len(nums))

        dp[0] = nums[0]
        dp[1] = max(nums[0] , nums[1])

        for house in range(2, len(nums)):
            dp[house] = max(dp[house-2]+nums[house] , dp[house-1])

        return dp[-1]       


algorithm = Solution()
nums = [10,7,29,300,1]
print(algorithm.rob(nums))