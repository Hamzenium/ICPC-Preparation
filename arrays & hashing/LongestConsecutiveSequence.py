class Solution(object):
    def longestConsecutive(self, nums):
        # sortedList = sorted(nums)
        # counter = 1
        # largest = 1
        # for i in range(len(nums)-2):
        #     if sortedList[i + 1]  - sortedList[i]  == 1:
        #         counter =  counter + 1
        #         if counter >  largest :
        #             largest = counter
        #     else:
        #         counter = 0
        # return largest
        res = 0
        store = set(nums)

        for num in nums:
            streak, curr = 0, num
            while curr in store:
                streak += 1
                curr += 1
            res = max(res, streak)
        return res



nums = [100,4,200,1,3,2]
sol = Solution()
print(sol.longestConsecutive(nums))