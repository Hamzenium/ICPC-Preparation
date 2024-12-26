class Solution(object):
    def twoSum(self, nums, target):
        dict = {}
        for i, j in enumerate(nums):
            diff = target - j
            if diff in dict:
                return [dict[diff], i]
            dict[j] = i
        return



class bruteforce(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i] + nums[j] == target:
                    return [i,j]
    
nums = [2,7,11,15]
target = 9
solution = Solution()
print(solution.twoSum(nums,target))