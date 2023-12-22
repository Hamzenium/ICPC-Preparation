class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        preFix = []
        postFix = [1] * len(nums)
        output = [1] * len(nums)
        sum = 1
        for index in range(len(nums)):
            if index == 0:
                preFix.append(nums[index])
            else:
                preFix.append(preFix[index-1] * nums[index])

        for index in range(len(nums)-1, -1, -1):
            if index == len(nums) - 1:
                postFix[index] = nums[index]
            else:
                postFix[index] = postFix[index+1] * nums[index]
        
        for index in range(len(nums)):
            counter = index - 1
            counter1 = index + 1
            if index == 0:
                output[index] = 1 * postFix[counter1]
            elif index == len(nums)-1:
                 output[index] = preFix[counter] * 1
            else:
                output[index] = preFix[counter] * postFix[counter1]

        return output, preFix, postFix




sol = Solution()
nums = [1,2,3,4]
print(sol.longestConsecutive(nums))