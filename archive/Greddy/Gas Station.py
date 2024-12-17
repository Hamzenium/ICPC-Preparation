class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        for i in range(len(gas)):
            total = 0
            number = 0
            if gas[i] - cost[i] > 0:
                total = cost[i] - gas[i]
                if number + 1 > len(cost) - 1:
                    number % len(cost) - 1
                else:
                    number = i + 1
                while number == i:
                    total = cost[i] - gas[i]

        return

                
sol = Solution()
gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
print(sol.canCompleteCircuit(gas,cost))