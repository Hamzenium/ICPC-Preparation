class Solution(object):
    def numIslands(self, grid):
        counter = 0
        if not grid:
            return 0
        row , col = len(grid) , len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    self.depth_first_search(grid, i , j)
                    counter += 1
        return counter
                
        
    def depth_first_search(self,grid ,i,j):

        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = "#"
        self.depth_first_search(grid,i+1,j)
        self.depth_first_search(grid,i-1,j)
        self.depth_first_search(grid,i,j+1)
        self.depth_first_search(grid,i,j-1)


algorithm = Solution()
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

print(algorithm.numIslands(grid))
