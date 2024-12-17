class Solution:
    def arraySign(self, nums: List[int]) -> int:
        index=1
        for i in range(len(nums)):
            index = index * nums[i]
        if index > 0:
            return 1
        elif index == 0:
            return 0
        else:
            return -1
        