from collections import defaultdict


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        num_dict = defaultdict(int)
        for i in range(len(nums)):
            if nums[i] in num_dict and abs(i - num_dict[nums[i]]) <= k:
                return True
            num_dict[nums[i]] = i
        return False


class BruteForce(object):
    def containsNearbyDuplicate(self, nums, k):
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] == nums[j] and i != j and abs(i - j) <= k:
                    return True
        return False


        

nums = [1,2,3,1]
k = 3
sol = Solution()
print(sol.containsNearbyDuplicate(nums,k))