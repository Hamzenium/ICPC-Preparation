class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        result = [[] for i in range(len(nums))]
        for i in range(len(nums)):
            w = (i + k) % len(nums)
            result[w] = nums[i]
        return result

nums = [-1,-100,3,99]
k = 2
solution = Solution()
print(solution.rotate(nums, k))