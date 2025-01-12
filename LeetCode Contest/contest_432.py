class Solution(object):
    def zigzagTraversal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        m, n = len(grid), len(grid[0])
        result = []
        skip = False  # Initialize a flag to skip alternate cells
        
        for i in range(m):
            if i % 2 == 0:  # Even rows: left to right
                for j in range(n):
                    if not skip:
                        result.append(grid[i][j])
                    skip = not skip  # Toggle the skip flag
            else:  # Odd rows: right to left
                for j in range(n - 1, -1, -1):
                    if not skip:
                        result.append(grid[i][j])
                    skip = not skip  # Toggle the skip flag
        
        return result