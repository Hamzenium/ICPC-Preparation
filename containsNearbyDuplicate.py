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