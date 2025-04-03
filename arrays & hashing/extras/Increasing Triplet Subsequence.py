class Solution(object):
    def increasingTriplet(self, nums):

        first = float('inf')
        second = float('inf')
        for i in range(len(nums)):
            if nums[i] < first:
                first= nums[i]
            elif nums[i] < second:
                second = nums[i]
            else:
                return True
        return False


nums = [1,2,3,4,5]
sol = Solution()
print(sol.increasingTriplet(nums))