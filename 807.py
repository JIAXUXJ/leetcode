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
            
        for i in range(len(grid)):
            vertical_max_value = grid[0][i]
            for j in range(len(grid)):
                if(grid[j][i] >= vertical_max_value):
                    vertical_max_value = grid[j][i]
            vertical.append(vertical_max_value)
        
        total, new  =  0, 0
        for i in range(len(grid)):
            for j in range(0, len(grid)):
                if(horizontal[i] <= vertical[j]):
                    new = horizontal[i]
                else:
                    new = vertical[j]
                total = total + (new - grid[i][j])

        return total