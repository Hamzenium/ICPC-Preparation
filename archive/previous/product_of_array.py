class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        array = [i for i in nums] # deep copy of the arrary 
        length = len(nums)-1
        for index in range(len(nums)):
          sum = 1
          while length != -1:
            if index == length : sum = sum
            else: sum *= nums[length]
            length = length - 1
          array[index] = sum
          length = len(nums)-1

        return array
    def productExceptSelf_better(self, nums):

      n = len(nums)
      result = [1] * n
      product = 1
      zero_count = 0

      # Calculate the total product and count the number of zeros
      for num in nums:
          if num != 0:
              product *= num
          else:
              zero_count += 1

      # If there's more than one zero, all results will be zero
      if zero_count > 1:
          return [0] * n

      # If there's exactly one zero, only its corresponding result will be non-zero
      if zero_count == 1:
          for i in range(n):
              if nums[i] == 0:
                  result[i] = product
              else:
                  result[i] = 0
      else:
          # No zeros, divide the total product by each element
          for i in range(n):
              result[i] = product // nums[i]

      return result

    
nums = [-1,1,0,-3,3]
soloution = Solution()
print(soloution.productExceptSelf(nums))
