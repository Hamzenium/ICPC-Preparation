

        
class BruteForce(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        res = [0] * n
        for i in range(n):
            prod = 1
            for j in range(n):
                if i == j:
                    continue    
                prod *= nums[j]
            
            res[i] = prod
        return res







nums = [1,2,3,4]
sol = Solution()
sol.productExceptSelf(nums)