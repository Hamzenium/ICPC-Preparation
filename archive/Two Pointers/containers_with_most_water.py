class Solution(object):
    def maxArea(self, height):
        left = 0
        sum = 0
        right = len(height)-1
        while left < right:
            x  = min(height[left],height[right]) 
            y = right - left
            product = x * y
            if product > sum:
                sum = product
            if height[left] < height[right]:
                left = left + 1
            elif height[right] <= height[left]:
                right = right - 1
        return sum

algorithm = Solution()
height = [1,8,6,2,5,4,8,3,7]
print(algorithm.maxArea(height))