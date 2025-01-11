class Solution(object):
    def longestConsecutive(self, nums):
        res = 0
        store = set(nums)

        for num in nums:
            streak, curr = 0, num
            while curr in store:
                streak += 1
                curr += 1
            res = max(res, streak)
        return res

class Solution:
    def longestConsecutive(self, nums):
        numSet = set(nums)
        longest = 0
        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest

nums = [100,4,200,1,3,2]
sol = Solution()
print(sol.longestConsecutive(nums))