class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if nums[i] + nums[j] == target and i != j:
        #             return [i,j]
        hashset = {}
        for index in range(len(nums)):
            result = nums[index]
            hashset[result] = index
        for index in range(len(nums)):
            diff = target - nums[index]
            if diff in hashset:
                if hashset[diff] != index:
                    return [index,hashset[diff]]
            
nums = [1,3,2,5]
algorithm = Solution()
algorithm.twoSum(nums,5)