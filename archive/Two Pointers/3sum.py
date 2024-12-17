class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        for i, a in enumerate(nums):
            print(i,a)
    
solution = Solution()
nums = [-1,0,1,2,-1,-4]
print(solution.threeSum(nums))