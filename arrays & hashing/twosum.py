


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