class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        low_value = min(prices)
        index = prices.index(low_value)
        array = [ i for i in prices]
        if index == len(prices) - 1:
             array.pop(index)
             low_value = min(array)
             index = array.index(low_value)

        sum = 0
        for i in range(len(prices) - 1, -1, -1):
            if prices[i] - prices[index] > sum and i > index:
                sum = prices[i] - prices[index]
        return sum



solution = Solution()
s = [3,2,6,5,0,3]
print(solution.maxProfit(s))

