class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        New = [[0] * len(grid[0]) for _ in range(len(grid))] 
        top = [max(grid[rows][cols] for rows in range(len(grid))) for cols in range(len(grid[0]))]
        left = [max(grid[rows][cols] for cols in range(len(grid[0]))) for rows in range(len(grid))]
        for row, row_max in enumerate(left):
            for col, col_max in enumerate(top):
                New[row][col] = min(row_max, col_max)
        return sum(New[row][col] - grid[row][col] for row in range(len(left)) for col in range(len(top)))