class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        horizontal, vertical = list(), list()
        for i in range(len(grid)):
            horizontal_max_value = grid[i][0]
            for j in range(len(grid)):
                if(grid[i][j] >= horizontal_max_value):
                    horizontal_max_value = grid[i][j]
            horizontal.append(horizontal_max_value)