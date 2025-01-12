class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height) - 1
        highest = 0
        while l < len(height) - 1 and r > 0:
            total = min(height[l], height[r])
            sum = total * (r - l)
            highest = max(sum,highest)
            if height[l + 1] > height[r - 1]:
                l = l + 1
            else:
                r = r -1
        return highest
                
class BruteForce:
    def maxArea(self, heights):
        res = 0
        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                res = max(res, min(heights[i], heights[j]) * (j - i))
        return res
height = [1,2,4,3]
solution = Solution()
print(solution.maxArea(height))