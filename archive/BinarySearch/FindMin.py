class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0 , len(nums)-1
        while left <= right:
            middle = (left + right ) // 2
            if left == right:
                return nums[left]
            elif nums[middle] > nums[right]:
                left = middle + 1
            else:
                right = middle
                

solution = Solution()
nums = [3,4,5,1,2]
print(solution.findMin(nums))