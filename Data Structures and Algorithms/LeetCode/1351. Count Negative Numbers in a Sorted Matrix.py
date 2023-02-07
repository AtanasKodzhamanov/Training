class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        row = len(grid)-1
        col = len(grid[0])-1
        count = 0
        for i in range(row, -1, -1):
            for j in range(col+1):
                if grid[i][j] < 0:
                    count += col-j+1
                    break
        return count
