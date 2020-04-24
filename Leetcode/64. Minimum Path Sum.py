from typing import List
import sys


class Solution:
    def __init__(self):
        self.min_sum = sys.maxsize

    def minPathSum(self, grid: List[List[int]], i=0, j=0, pc=0) -> int:
        if 0 <= i < len(grid) and 0 <= j < len(grid[0]):
            print(grid[i][j], end=' ')
            if pc + grid[i][j] >= self.min_sum:
                print('\t', self.min_sum, '\n')
                return self.min_sum

            if i == len(grid) - 1 and j == len(grid[0]) - 1:
                self.min_sum = pc + grid[i][j]
                print('\t', self.min_sum, '\n')

            self.minPathSum(grid, i + 1, j, pc + grid[i][j])
            self.minPathSum(grid, i, j + 1, pc + grid[i][j])
        return self.min_sum


# O(N*M) Recursion
class Solution2:
    def minPathSum(self, grid: List[List[int]], i=0, j=0, visited_grid=None) -> int:
        if not visited_grid:
            visited_grid = [[False for x in range(len(grid[0]))] for y in range(len(grid))]

        if i == len(grid) or j == len(grid[0]):
            return sys.maxsize

        if (i == len(grid) - 1 and j == len(grid[0]) - 1) or visited_grid[i][j]:
            return grid[i][j]

        visited_grid[i][j] = True
        bottom = self.minPathSum(grid, i + 1, j, visited_grid)
        right = self.minPathSum(grid, i, j + 1, visited_grid)

        grid[i][j] += min(bottom, right)
        return grid[i][j]


# O(N*M) Loop
class Solution3:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row = len(grid) - 1

        while row > -1:
            col = len(grid[0]) - 1
            while col > -1:
                if row + 1 < len(grid) and col + 1 < len(grid[0]):
                    grid[row][col] += min(grid[row + 1][col], grid[row][col + 1])
                elif row + 1 < len(grid):
                    grid[row][col] += grid[row + 1][col]
                elif col + 1 < len(grid[0]):
                    grid[row][col] += grid[row][col + 1]

                col -= 1
            row -= 1

        return grid[0][0]


sol = Solution3()
grid = [
    [0, 7, 7, 8, 1, 2, 4, 3, 0, 0, 5, 9, 8, 3, 6, 5, 1, 0],
    [2, 1, 1, 0, 8, 1, 3, 3, 9, 9, 5, 8, 7, 5, 7, 5, 5, 8],
    [9, 2, 3, 1, 2, 8, 1, 2, 3, 7, 9, 7, 9, 3, 0, 0, 3, 8],
    [3, 9, 3, 4, 8, 1, 2, 6, 8, 9, 3, 4, 9, 4, 8, 3, 6, 2],
    [3, 7, 4, 7, 6, 5, 6, 5, 8, 6, 7, 3, 6, 2, 2, 9, 9, 3],
    [2, 3, 1, 1, 5, 4, 7, 4, 0, 7, 7, 6, 9, 1, 5, 5, 0, 3],
    [0, 8, 8, 8, 4, 7, 1, 0, 2, 6, 1, 1, 1, 6, 4, 2, 7, 9],
    [8, 6, 6, 8, 3, 3, 5, 4, 6, 2, 9, 8, 6, 9, 6, 6, 9, 2],
    [6, 2, 2, 8, 0, 6, 1, 1, 4, 5, 3, 1, 7, 3, 9, 3, 2, 2],
    [8, 9, 8, 5, 3, 7, 5, 9, 8, 2, 8, 7, 4, 4, 1, 9, 2, 2],
    [7, 3, 3, 1, 0, 9, 4, 7, 2, 3, 2, 6, 7, 1, 7, 7, 8, 1],
    [4, 3, 2, 2, 7, 0, 1, 4, 4, 4, 3, 8, 6, 2, 1, 2, 5, 4],
    [1, 9, 3, 5, 4, 6, 4, 3, 7, 1, 0, 7, 2, 4, 0, 7, 8, 0],
    [7, 1, 4, 2, 5, 9, 0, 4, 1, 4, 6, 6, 8, 9, 7, 1, 4, 3],
    [9, 8, 6, 8, 2, 6, 5, 6, 2, 8, 3, 2, 8, 1, 5, 4, 5, 2],
    [3, 7, 8, 6, 3, 4, 2, 3, 5, 1, 7, 2, 4, 6, 0, 2, 5, 4],
    [8, 2, 1, 2, 2, 6, 6, 0, 7, 3, 6, 4, 5, 9, 4, 4, 5, 7]]

grid2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(sol.minPathSum(grid))
for g in grid2:
    print(g)
