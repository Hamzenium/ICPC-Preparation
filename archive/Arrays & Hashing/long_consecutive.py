class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        7:10
        """
        if len(nums) == 0:
            return 0
        new_list = sorted(nums)
        counter = 0
        answer = 0
        for i in range(len(new_list)):
            if i < len(nums) - 1:
                if new_list[i+1] - new_list[i] == 1 :
                    counter = counter + 1
                    if counter >= answer:
                        answer = counter
                elif new_list[i+1] - new_list[i] == 0 :
                    counter =  counter  + 0
                else:
                    if counter > answer:
                        answer = counter
                    counter  = 0
        return answer+1


sol = Solution()
nums = [1,2,0,1]
print(sol.longestConsecutive(nums))