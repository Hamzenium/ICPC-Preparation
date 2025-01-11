from collections import defaultdict


class Solution(object):
    def threeSum(self,nums):
        output = []
        seen = defaultdict(int)
        
        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    if i != j and i != k and j != k:
                        if nums[i] + nums[j] + nums[k] == 0:
                            triplet = sorted([nums[i], nums[j], nums[k]])
                            # To avoid duplicates, use a set to track already found triplets
                            if tuple(triplet) not in seen:
                                output.append(triplet)
                                seen[tuple(triplet)] = 1
        return output