class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
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

        return output

            

solution = Solution()
nums = [-1,1,0,-3,3]
print(solution.productExceptSelf(nums))


#time complexity of the algorithm is O(n^2)

# class Solution(object):
#     def productExceptSelf(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         array = []
#         length = len(nums) - 1
#         sum = 1
#         for index in range(len(nums)):
#             while length != 0:
#                 if index == length:
#                     length = length -1
#                     continue
#                 else:
#                     sum *= nums[length]
#                     length = length - 1
#             array.append(sum)
#             sum = 1
#             length = len(nums) - 1
#         return array        