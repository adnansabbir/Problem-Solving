from typing import List


class Solution:
    def mark_connected(self, grid, i, j):
        if 0 <= i < len(grid) and 0 <= j < len(grid[0]):
            if grid[i][j] == '1':
                grid[i][j] = '2'
                self.mark_connected(grid, i - 1, j)
                self.mark_connected(grid, i + 1, j)
                self.mark_connected(grid, i, j + 1)
                self.mark_connected(grid, i, j - 1)

    def numIslands(self, grid: List[List[str]]) -> int:
        island_counter = 0
        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                if col == '1':
                    self.mark_connected(grid, i, j)
                    island_counter += 1
        return island_counter


def splitter(s):
    return [x for x in s]


sol = Solution()
grid = [
    splitter('111'),
    splitter('000'),
    splitter('111'),
]
print(sol.numIslands(grid))
