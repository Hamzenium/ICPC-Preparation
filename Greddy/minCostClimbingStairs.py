class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        if not cost:
            return 0
        dp = [0] * len(cost)
        dp[0] = cost[0]
        if len(cost) >= 2:
            dp[1] = cost[1]
        for i in range(2,len(cost)):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])

        return min(dp[-1], dp[-2])


sol = Solution()
n = [0,1,2,2]
o = [0,1,2,2,0]
q = [1,100,1,1,1,100,1,1,100,1]
print(sol.minCostClimbingStairs(q))


def minCostClimbingStairs(self, cost):
    """
    :type cost: List[int]
    :rtype: int
    """
    counter = -1
    value = 0
    length = len(cost) - 1
    if len(cost) == 3:
        if cost[0] + cost[2] < cost[1]:
            return cost[1]
        else:
            return cost[0] + cost[2]
    while counter < length:
        if counter == -1:
            if cost[0] < cost[1]:
                counter = 0
                value += cost[0]
            else:
                counter = 1
                value += cost[1]
        elif counter + 2 > len(cost) - 1:
            return value
        elif cost[counter + 1] < cost[counter + 2]:
            value += cost[counter + 1]
            counter = counter + 1
        else:
            value += cost[counter +2]
            counter = counter + 2
    return value