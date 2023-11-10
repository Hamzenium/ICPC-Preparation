class Solution(object):
    def missingNumber(self, nums):
        nums.sort()
        counter = 0
        for i in nums:
            if int(i) != int(counter):
                return counter
            counter = counter + 1
        return counter
        

            
