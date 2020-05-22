from typing import List

class Solution:

    @staticmethod
    def calculateSquares(matrix, r, c):
        height = len(matrix) - 1
        width = len(matrix[0]) - 1

        if not matrix[r][c]:
            return 0
        elif r >= height or c >= width:
            return 1
        else:
            return min(matrix[r + 1][c], matrix[r + 1][c + 1], matrix[r][c + 1]) + 1

    def countSquares(self, matrix: List[List[int]]) -> int:
        row = len(matrix) - 1
        column = len(matrix[0]) - 1
        total_squares = 0
        for r in range(row, -1, -1):
            for c in range(column, -1, -1):
                matrix[r][c] = self.calculateSquares(matrix, r, c) if matrix[r][c] else matrix[r][c]
                total_squares += matrix[r][c]

        return total_squares