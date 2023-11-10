class Solution(object):
    def largestPerimeter(nums):
        i=0
        j=1
        k=2
        nums.sort(reverse=True)
        if len(nums)==3 and nums[0] < nums[1] + nums[2]:
            return sum(nums)
        elif len(nums) > 3:
            while i < len(nums) and j < len(nums) and k < len(nums):
                if nums[i] < nums[i+1] +nums[i+2]:
                   return nums[i]+nums[i+1]+nums[i+2]
                else:
                    i=i+1
                    j=j+1
                    k=k+1
        return 0
        
    nums = [1,1,5,2,3]
    print(largestPerimeter(nums))
# time complexity is O(n)
