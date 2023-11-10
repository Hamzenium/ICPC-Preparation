class Solution(object):
    def permute(self, nums):
        res = []
        while len(res) < math.factorial(len(nums)):
            random.shuffle(nums)
            if nums not in res:
                res.append(nums[:])
        return res
