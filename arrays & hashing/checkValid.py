class Solution(object):
    def checkValid(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        dict = set(range(1,len(matrix)+1))
        for row in matrix:
            check = set(row)
            if check != dict:
                return False
        for col in zip(matrix):
            check = set(col)
            if check != dict:
                return False
        return True

class BruteForce(object):
    def checkValid(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        for i in matrix:
            seen = set()
            for j in i:
                if j in seen and len(seen) > 0:
                    return False
                else:
                    seen.add(j)
        return True

sol = Solution()
matrix = [[1,1,1],[1,2,3],[1,2,3]]
print(sol.checkValid(matrix))